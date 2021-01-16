
import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

textwidth_in = 6.69423
figsize = [textwidth_in * 0.8, textwidth_in * .5]


model = 'GVAE'
permutation = '1'
delta = '_delta'

ip_name = '{}_fb15k_p{}{}'.format(model, permutation, delta)

with open('data/ip/{}.json'.format(ip_name), 'r') as f:
    all_dict = json.load(f)

ip_between2 = all_dict['interpolations.between2.text']

with open('data/ip/{}.txt'.format(ip_name), 'w+') as f:
    for n in range(10):
        f.writelines('\\texttt{'+str(ip_between2[n]).replace('_','\\_').replace('\'','').replace(', ','] [')+'}\\\\\n')


# ip_dims = [all_dict['interpolations.confi95.text.{}'.format(n for n in range(10))]]

# val = list()
# bin = list()
# lay = list()
# cod = list()
# for coder in ['encoder.mlp', 'decoder.rmlp']:   #
#     for layer in [0, 3, 5]:
#         val.extend(all_dict['gradients/{}.{}.weight'.format(coder, str(layer))]['values'])
#         bin.extend(all_dict['gradients/{}.{}.weight'.format(coder, str(layer))]['bins'][1:])
#         lay.extend([str(layer)]*len(all_dict['gradients/{}.{}.weight'.format(coder, str(layer))]['values']))
#         cod.extend([coder.split('.')[0].capitalize() ]*len(all_dict['gradients/{}.{}.weight'.format(coder, str(layer))]['values']))
#     if coder == 'encoder.mlp':
#         lay.reverse()

# df = pd.DataFrame(columns=['vals','bins','layer','part'],)
# df['vals'] = val
# df['bins'] = bin
# df['layer'] = lay
# df['part'] = cod
# bin_min, bin_max = df.bins.min(), df.bins.max()
# v_max = float(df.vals.max())

# part = 'decoder'
# palette = 'summer'            # https://medium.com/@morganjonesartist/color-guide-to-seaborn-palettes-da849406d44f PRGn YlGn viridis_r
# palette_r = 'summer_r'
# for part in ['encoder']: 
#     df_plot = df.loc[df['part'] == part]
#     sns.set()
#     sns.set_context("paper")

#     g = sns.relplot(data=df, x="bins", y="vals", hue="layer", col="part", palette=palette, height=figsize[1], aspect=figsize[0]/figsize[1], kind="line")

#     g.set(yscale = 'log')
#     g.set(xlabel='Bins', ylabel='Values')
#     g.set(xlim=(bin_min, bin_max))
#     plt.tight_layout()
#     plt.savefig('data/ip/{}_{}.png'.format(ip_name, part))
#     plt.close()

