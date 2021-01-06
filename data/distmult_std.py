import numpy as np
import pandas as pd


df = pd.DataFrame(columns=['model','MRR_mean','MRR_std','H1_mean','H1_std','H3_mean','H3_std','H10_mean','H10_std'])

mrr = [0.2837, 0.2889, 0.2836]
h1 = [0.1992,0.2015,0.1994]
h3 = [0.3127,0.3202,0.3117]
h10 = [0.4473,0.4587,0.4475]
df.loc[0] = ['Original',np.mean(mrr),np.std(mrr),
            np.mean(h1),np.std(h1),np.mean(h3),np.std(h3),np.mean(h10),np.std(h10),]

mrr = [0.0005404,0.0005186,0.0004921]
h1 = [0.00002443,0,0.00004886]
h3 = [0.0001222,0.00007329,0.00004886]
h10 = [0.0004398,0.0004398,0.0003176]
df.loc[1] = ['Variational',np.mean(mrr),np.std(mrr),
            np.mean(h1),np.std(h1),np.mean(h3),np.std(h3),np.mean(h10),np.std(h10),]

mrr = [0.0005942,0.0006438,0.0006814]
h1 = [0.00002443,0.00004886,0.00009772]
h3 = [0.00004886,0.0001222,0.0002932]
h10 = [0.0006596,0.0006352,0.0006108]
df.loc[2] = ['Var.wELBO',np.mean(mrr),np.std(mrr),
            np.mean(h1),np.std(h1),np.mean(h3),np.std(h3),np.mean(h10),np.std(h10),]

# df = df.round(decimals=4)
print(df.head)
df.to_csv('data/varDistmult_scores.csv')

