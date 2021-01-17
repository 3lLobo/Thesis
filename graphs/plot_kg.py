import matplotlib
import matplotlib.pylab as plt
import os
from matplotlib.pyplot import legend, title
from numpy.core.defchararray import array
from numpy.lib.shape_base import column_stack
import seaborn as sns
import pandas as pd
import itertools
import numpy as np




def plot_graph(data, plot_name, figsize, legend):
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

    g = sns.catplot(data=data, kind="bar", x='Model', y='Score', hue="Loss", ci='sd', palette=palette, legend=legend, legend_out=True, height=figsize[1], aspect=figsize[0]/figsize[1])
    g.despine(left=True)
    g.set(ylim=(0, .5))
    g.map(plt.axhline, y=0.3633, color='purple', linestyle='dotted')
    # plt.legend(loc='upper right', title='Metric')
    g.set(xlabel='', ylabel='Score')
    # plt.title(t_name.replace('_', ' ').title())
    folder = os.path.dirname(os.path.abspath(__file__)) + '/plots/'
    if not os.path.isdir(folder):
        os.makedirs(folder)
    # plt.savefig(folder + '{}.pgf'.format(plot_name))
    g.savefig(folder + '{}{}.png'.format(plot_name, '' if legend else '_wol'))
    # plt.savefig(folder + '{}{}.png'.format(plot_name, '' if legend else '_wol'))



if __name__ == "__main__":
    
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

    std = 'all'
    # col_names = ['hits@1','hits@10','hits@3','mrr']
    # temp_names =['']
    df_list = list()
    df_plot = pd.DataFrame()
    legend = True
    # for std in ['', 'std2']:
    #     if std == 'std2':
    #         legend = False
    plot_name = 'kg_{}'.format(std)
    textwidth_in = 6.69423
    figsize = [textwidth_in * 0.8, textwidth_in * .5]


    # df_1 = pd.read_csv('graphs/data/kg_valid.csv')
    # df_1.drop([col for col in df_1.columns if ('__MIN' in col or '__MAX' in col or 'Step' in col)], axis=1, inplace=True)

    # # df_temp = df_1[[col for col in df_1.columns if '_temp' in col ]]
    # # df_temp.drop([col for col in df_temp.columns if ('__MIN' in col or '__MAX' in col)], axis=1, inplace=True)
    # # std = df_temp.std(axis=0).to_list()
    # # std = np.array(std[-1:]+std[:-1])
    # # col_names = ['score','model', 'loss', 'std']
    # for col in df_1.columns:
        
    #         df_append = pd.DataFrame()
    #         df_append['Score'] = df_1[col]
    #         df_append['Model'] = ['RGVAE' if 'GVAE' in col else 'cRGVAE'] * len(df_append)
    #         if 'std' in col:
    #             df_append['Loss'] = ['permute sigma2' if 'p1' in col else 'standard sigma2'] * len(df_append)
    #         else:
    #             df_append['Loss'] = ['permute sigma1' if 'p1' in col else 'standard sigma1'] * len(df_append)
    #         df_list.append(df_append)
    # df_plot = pd.concat(df_list, axis=0)

    # df_plot.to_csv('graphs/data/kg/kg_{}.csv'.format(std))


    df_plot = pd.read_csv('graphs/data/kg/kg_{}.csv'.format(std))
    print('Total {}'.format(len(df_plot)))
    # df_plot.mrr = df_plot.mrr * 500

    # df2.to_csv('beta_plot.csv')
    plot_graph(df_plot, plot_name, figsize, legend)