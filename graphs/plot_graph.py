import matplotlib
import matplotlib.pylab as plt
import os
from matplotlib.pyplot import title
import seaborn as sns
import pandas as pd
from seaborn import palettes



def plot_graph(data, plot_name, figsize):
    """
    Plot the input data to latex compatible .pgg format.
    """
    sns.set()
    sns.set_context("paper")
    sns.set(rc={'figure.figsize':figsize})
    palette = 'cool'            #['copper_r', 'BuPu'afmhot_r cool_r] https://medium.com/@morganjonesartist/color-guide-to-seaborn-palettes-da849406d44f
    # sns.color_palette("viridis", as_cmap=True)
    # sns.set_palette(sns.color_palette("icefire", as_cmap=True))
    # sns.set_palette(palette='bupu')
    fig, ax = plt.subplots(figsize=figsize)
    sns.lineplot(ax=ax, data=data, x="epoch", y="val_loss_mean", hue="beta", palette=palette)
    # fig, ax = plt.subplots()
    # ax.plot(*list(zip(*sorted(loss_dict['val'].items()))), 'g', label='Validation loss')
    # ax.plot(*list(zip(*sorted(loss_dict['train'].items()))), 'b', label='Training loss')

    plt.legend(loc='upper right', title='beta')
    plt.title(plot_name)
    plt.xlabel('Epoch')
    plt.ylabel('Elbo')
    plt.show()
    folder = os.path.dirname(os.path.abspath(__file__)) + '/plots/'
    if not os.path.isdir(folder):
        os.makedirs(folder)
    # plt.savefig(folder + '{}.pgf'.format(plot_name))
    plt.savefig(folder + '{}.png'.format(plot_name))



if __name__ == "__main__":
    
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', -1)

    ds = 'wn'
    plot_name = 'beta_{}'.format(ds)
    textwidth_in = 6.69423
    figsize = [textwidth_in * 0.8, textwidth_in * .7]
    beta_list = [0,1,10,100]
    df_list = list()
    for beta in beta_list:
        df_1 = pd.read_csv('graphs/data/beta_{}_all_b{}.csv'.format(ds, beta))
        df_1.drop([col for col in df_1.columns if ('__MIN' in col or '__MAX' in col)], axis=1, inplace=True)
        
        col_dict = dict(zip(df_1.columns, ['step','val_loss_mean','mrr','epoch']))
        
        df_1 = df_1.rename(columns=col_dict)
        df_1.fillna(method='bfill', inplace=True)
        df_1['beta'] = [str(beta)] * len(df_1)
        df_list.append(df_1)



    # df_1 = pd.read_csv('graphs/data/beta_wn_valloss.csv')
    # df_e = pd.read_csv('graphs/data/beta_wn_valloss.csv')
    # df = pd.DataFrame.merge(df_1, df_e, on='_step')
    # name_list = []
    # beta_list = [0,1,10,100] 
    # df_list = []

    df_plot = pd.concat(df_list, axis=0)
    print('Total {}'.format(len(df_plot)))

    # df2.to_csv('beta_plot.csv')
    plot_graph(df_plot, plot_name, figsize)