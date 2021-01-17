import matplotlib
import matplotlib.pylab as plt
import os
from matplotlib.pyplot import legend, title
from numpy.core.defchararray import array
import seaborn as sns
import pandas as pd
import itertools
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
    sns.set_context("paper")
    # sns.set(rc={'figure.figsize':figsize})
    palette = 'summer'            #['copper_r', 'BuPu'afmhot_r cool_r] https://medium.com/@morganjonesartist/color-guide-to-seaborn-palettes-da849406d44f

    sns.set_theme(style="whitegrid")

    g = sns.catplot(data=data, kind="bar", x='model', y='score', hue="Metric", ci='sd', palette=palette, legend=legend, legend_out=True, height=figsize[1], aspect=figsize[0]/figsize[1])
    g.despine(left=True)
    g.set(ylim=(0, .1))
    # plt.legend(loc='upper right', title='Metric')
    plt.xlabel('')
    plt.ylabel('Score')
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

    col_names = ['hits@1','hits@10','hits@3','mrr']
    legend = True
    for ds in ['fb', 'wn']:
        temp_names =['']
        df_list = list()
        df_plot = pd.DataFrame()
        if ds == 'wn':
            legend = False
        plot_name = 'lp_{}'.format(ds)
        textwidth_in = 6.69423
        figsize = [textwidth_in * 0.8, textwidth_in * .5]
        for model in ['GVAE', 'GCVAE']:

            df_1 = pd.read_csv('graphs/data/LP/lp_{}_{}.csv'.format(model, ds))
            df_temp = df_1[[col for col in df_1.columns if '_temp' in col ]]
            df_temp.drop([col for col in df_temp.columns if ('__MIN' in col or '__MAX' in col)], axis=1, inplace=True)
            std = df_temp.std(axis=0).to_list()
            std = np.array(std[-1:]+std[:-1])


            df_1.drop([col for col in df_1.columns if ('__MIN' in col or '__MAX' in col or '_temp' in col)], axis=1, inplace=True)
            df_1.drop(['Step'], axis=1, inplace=True)
            df_1 = df_1.rename(columns=dict(zip(df_1.columns, col_names)))
            scale = .5 if ds == 'fb' else .6
            for n in [0, scale,-scale]:
                df_plot['score'] = np.array(df_1.stack([0]).to_list()) + n*std
                df_plot['model'] = [model] * len(df_plot)
                df_plot['Metric'] = col_names
                df_list.append(df_plot.copy())
            
            # df_1.fillna(method='bfill', inplace=True)
            # df_list.append(df_1.loc([metric]) for metric in col_names)

        df_plot = pd.concat(df_list, axis=0)
        df_plot.to_csv('graphs/data/LP/lp_{}.csv'.format(ds))
        print('Total {}'.format(len(df_plot)))
        # df_plot.mrr = df_plot.mrr * 500

        # df2.to_csv('beta_plot.csv')
        plot_graph(df_plot, col_names, plot_name, figsize, legend)