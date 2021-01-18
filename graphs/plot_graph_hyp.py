import matplotlib
import matplotlib.pylab as plt
import os
from matplotlib.pyplot import title
import seaborn as sns
import pandas as pd
from seaborn import palettes



def plot_graph(data, metric, plot_name, figsize):
    """
    Plot the input data to latex compatible .pgg format.
    """
    sns.set()
    sns.set_context("paper")
    sns.set(rc={'figure.figsize':figsize})
    palette = 'summer'            #['copper_r', 'BuPu'afmhot_r cool_r] https://medium.com/@morganjonesartist/color-guide-to-seaborn-palettes-da849406d44f
    fig, ax = plt.subplots(figsize=figsize)
    if metric == 'mrr':
        sns.barplot(ax=ax, data=data, y=metric, x="beta", palette=palette)
        plt.xlabel('Beta')
        plt.ylabel('MRR')
        plt.ylim=(0, .1)
    elif metric == 'loss':
        sns.lineplot(ax=ax, data=data, y=metric, x="epoch", hue='beta', palette=palette)
        plt.legend(loc='upper right', title=r'$\beta$')
        plt.xlabel('Epoch')
        plt.ylabel('ELBO')
    # plt.title(t_name.replace('_', ' ').title())
    plt.show()
    folder = os.path.dirname(os.path.abspath(__file__)) + '/plots/'
    if not os.path.isdir(folder):
        os.makedirs(folder)
    # plt.savefig(folder + '{}.pgf'.format(plot_name))
    plt.savefig(folder + '{}.png'.format(plot_name), bbox_inches='tight')



if __name__ == "__main__":
    
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

    textwidth_in = 6.69423
    figsize = [textwidth_in * 0.8, textwidth_in * .5]
    for ds in ['fb', 'wn']:
        for metric in ['loss']:

            plot_name = 'beta_{}_{}'.format(metric, ds)
            
            beta_list = [0,1,10,100]
            df_list = list()
            for beta in beta_list:
                df_1 = pd.read_csv('graphs/data/beta/beta_{}_all_b{}.csv'.format(ds, beta))
                df_1.drop([col for col in df_1.columns if ('__MIN' in col or '__MAX' in col)], axis=1, inplace=True)
                
                col_dict = dict(zip(df_1.columns, ['step','loss','mrr','epoch']))
                
                df_1 = df_1.rename(columns=col_dict)
                df_1.fillna(method='bfill', inplace=True)
                df_1['beta'] = [str(beta)] * len(df_1)
                df_list.append(df_1)

            df_plot = pd.concat(df_list, axis=0)
            print('Total {}'.format(len(df_plot)))
            # df_plot.mrr = df_plot.mrr * 500

            # df2.to_csv('beta_plot.csv')
            plot_graph(df_plot, metric, plot_name, figsize)