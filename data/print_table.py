import pandas as import pd
import numpy as np


def mk_table(df, file_path):

    with open(file_path, 'w+') as f:
        f.writeline('\\begin\{table\}[H]\n \\centering\n \\begin\{tabular\}\{|{}\}'.format('l|'))


        \begin{table}[H]
  \centering
      \begin{tabular}{|l|l|l|l|l|}
      \hline
      \rowcolor[HTML]{EFEFEF}
      \multicolumn{1}{|c}{\textsc{Model}} & \multicolumn{1}{c}{\textsc{MRR}} & \multicolumn{1}{c}{\textsc{Hits@$1$}} & \multicolumn{1}{c}{\textsc{Hits@$3$}} & \multicolumn{1}{c|}{\textsc{Hits@$3$}} \\\hline
      DistMult     & \multicolumn{1}{c|}{$0.2854\pm 0.0025$} & \multicolumn{1}{c|}{$0.2\pm 0.001$} & \multicolumn{1}{c|}{$0.3149\pm 0.0038$} & \multicolumn{1}{c|}{$0.4512\pm 0.0053$}  \\
      VDistMult   & \multicolumn{1}{c|}{$0.517\pm 0.0197e^{-3}$} & \multicolumn{1}{c|}{$0.2442\pm 0.1994e^{-4}$} & \multicolumn{1}{c|}{$0.8145 \pm 0.3049e^{-4}$} & \multicolumn{1}{c|}{$0.399\pm 0.0576e^{-3}$} \\
      VDistMult w/ ELBO   & \multicolumn{1}{c|}{$0.6397\pm 0.0357e^{-3}$} & \multicolumn{1}{c|}{$0.57\pm 0.3046e^{-4}$} & \multicolumn{1}{c|}{$0.1547\pm 0.1023e^{-3}$} & \multicolumn{1}{c|}{$0.6351\pm 0.1992e^{-4}$} \\
      RGVAE w/o ELBO   & \multicolumn{1}{c|}{$0.1412$} & \multicolumn{1}{c|}{$0.0981$} & \multicolumn{1}{c|}{$0.1494$} & \multicolumn{1}{c|}{$0.2275$} \\
      \hline
      \end{tabular}
      \caption{Link prediction scores of DistMult and RGVAE versions on the FB15k-237 dataset.}
      \label{tab5:VarDistM}
  \end{table}
