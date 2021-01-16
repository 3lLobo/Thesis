
import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

textwidth_in = 6.69423
figsize = [textwidth_in * 0.8, textwidth_in * .35]


model = 'GVAE'
permutation = '0'
delta = '_delta'
param = 'bias'
for permutation in ['0', '1']:
    for delta in ['', '_delta']:
        for param in ['weight', 'bias']:
            ip_name = '{}_fb15k_p{}{}'.format(model, permutation, delta)

            with open('data/ip/{}.json'.format(ip_name), 'r') as f:
                all_dict = json.load(f)


            val = list()
            bin = list()
            lay = list()
            cod = list()
            for coder in ['encoder.mlp', 'decoder.rmlp']:   #
                for layer in [0, 3, 5]:
                    val.extend(all_dict['gradients/{}.{}.{}'.format(coder, str(layer), param)]['values'])
                    bin.extend(all_dict['gradients/{}.{}.{}'.format(coder, str(layer), param)]['bins'][1:])
                    lay.extend([str(layer)]*len(all_dict['gradients/{}.{}.{}'.format(coder, str(layer), param)]['values']))
                    cod.extend([coder.split('.')[0].capitalize() ]*len(all_dict['gradients/{}.{}.{}'.format(coder, str(layer), param)]['values']))
                # if coder == 'encoder.mlp':
                #     lay.reverse()

            df = pd.DataFrame(columns=['vals','bins','layer','part'],)
            df['vals'] = np.log([x if x!=0 else 1 for x in val])
            df['bins'] = bin
            df['layer'] = lay
            df['part'] = cod
            bin_min, bin_max = df.bins.min(), df.bins.max()
            v_max = float(df.vals.max())

            part = 'Decoder'
            palette = 'summer'            # https://medium.com/@morganjonesartist/color-guide-to-seaborn-palettes-da849406d44f PRGn YlGn viridis_r
            palette_r = 'summer_r'
            for part in ['Encoder']: 
                df_plot = df.loc[df['part'] == part]
                sns.set()
                sns.set_context("paper")

                # g = sns.relplot(data=df, x="bins", y="vals", hue="layer", col="part", palette=palette, height=figsize[1], aspect=figsize[0]/figsize[1], kind="line")
                g = sns.catplot(x="layer", y="bins", hue="vals", col='part', data=df, legend=False, palette=palette, height=figsize[1], aspect=figsize[0]/figsize[1],)

                # Make space for the colorbar
                # g.fig.subplots_adjust(right=.92)

                # Define a new Axes where the colorbar will go
                cax = g.fig.add_axes([.96, .25, .02, .5]) #[.94, .25, .02, .6])

                # Get a mappable object with the same colormap as the data
                points = plt.scatter([], [], c=[], vmin=0, vmax=v_max, cmap=palette)

                # Draw the colorbar
                g.fig.colorbar(points, cax=cax)
                g.set(xlabel='Bins', ylabel='Values')

                # g.set(yscale = 'log')
                # g.set(xlim=(bin_min, bin_max))
                # plt.tight_layout()
                plt.savefig('data/ip/scatter_{}_{}_{}.png'.format(ip_name, part, param), bbox_inches='tight')
                plt.close()

