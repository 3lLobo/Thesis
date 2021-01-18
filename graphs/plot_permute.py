import matplotlib
import matplotlib.pylab as plt
import os
import seaborn as sns
import pandas as pd
import numpy as np




def plot_graph(data, metric, plot_name, figsize, legend):
    """
    Plot the input data to latex compatible .pgg format.
    """
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    # sns.set()
    sns.set()
    sns.set_context("paper")
    sns.set(rc={'figure.figsize':figsize})
    # sns.set(rc={'figure.figsize':figsize})
    palette = 'summer'            #['copper_r', 'BuPu'afmhot_r cool_r] https://medium.com/@morganjonesartist/color-guide-to-seaborn-palettes-da849406d44f
    fig, ax = plt.subplots(figsize=figsize)

    sns.lineplot(ax=ax, data=data, x='Epoch', y=metric, hue='Model', ci=None, style='$\mathcal{L}$', palette=palette, legend=legend,)
    if legend:
        plt.legend(loc='upper right', bbox_to_anchor=(1.33, 1), frameon=False, facecolor='white')
    plt.xlabel('Epoch')
    plt.ylabel('ELBO' if metric=='loss' else 'Permutation rate')

    # g = sns.catplot(data=data, kind="line", x='epoch', y=metric, hue='model', style='$\mathcal{L}$', ci='sd', palette=palette, legend=legend, legend_out=True, height=figsize[1], aspect=figsize[0]/figsize[1])
    # g.despine(left=True)
    # g.set(ylim=(0, .1))
    # g.map(plt.axhline, y=baseline, color='purple', linestyle='dotted')
    # plt.legend(loc='upper right', title='Metric')
    # plt.title(t_name.replace('_', ' ').title())
    folder = os.path.dirname(os.path.abspath(__file__)) + '/plots/'
    if not os.path.isdir(folder):
        os.makedirs(folder)
    # plt.savefig(folder + '{}.pgf'.format(plot_name))
    plt.savefig(folder + '{}{}.png'.format(plot_name, '' if legend else '_wol'), bbox_inches='tight')



if __name__ == "__main__":
    
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

    df_1 = pd.read_csv('graphs/data/permute_all.csv')
    df_1.fillna(method='bfill', inplace=True)

    textwidth_in = 6.69423
    figsize = [textwidth_in * 0.8, textwidth_in * .5]
    df_1.drop([col for col in df_1.columns if ('__MIN' in col or '__MAX' in col or '_temp' in col)], axis=1, inplace=True)
    df_1.drop(['Step'], axis=1, inplace=True)
    for metric in ['loss', 'permutation']:
        plot_name = 'permute_{}'.format(metric)
        df_list = list()
        df_plot = pd.DataFrame(columns=[metric, 'Epoch', 'Model', '$\mathcal{L}$'])
        legend = True if metric=='loss' else False
        for model in ['GVAE', 'GCVAE']:
            for perm in ['p1','p0']:
                df = pd.DataFrame()
                cal2keep = [col for col in df_1.columns if (model in col and perm in col)]
                m_col = [col for col in cal2keep if metric in col]
                df[metric] = df_1[m_col[0]]
                df['Model'] = ['RGVAE' if model=='GVAE' else 'cRGVAE'] * len(df)
                df['$\mathcal{L}$'] = ['permute' if perm=='p1' else 'standard'] * len(df)
                e_col = [col for col in cal2keep if 'epoch' in col]
                df['Epoch'] = df_1[e_col[0]]
                df_list.append(df.copy())
        df_plot = pd.concat(df_list, axis=0)
        # df_plot.to_csv('graphs/data/LP/lp_{}.csv'.format(ds))
        print('Total {}'.format(len(df_plot)))
        # df_plot.mrr = df_plot.mrr * 500
                                                    
        # df2.to_csv('beta_plot.csv')
        plot_graph(df_plot, metric, plot_name, figsize, legend)
