import pandas as pd

class Dataset:
    df = pd.read_csv('C:\DATA\S2 UGM\Semester 2\KKPM\Tugas GA\MLBB_GenethicAlgorithm\dataset.csv', sep= ',')
    pd.set_option('display.float_format', '{:.2f}'.format)
    df['Id'] = df.reset_index().index + 1



    Gold = df[df['Lane'] == 'Gold Lane']
    Jungler = df[df['Lane'] == 'Jungler']
    Mid = df[df['Lane'] == 'Mid']
    Exp = df[df['Lane'] == 'EXP Lane']
    Roamer = df[df['Lane'] == 'Roamer']

    Gold.index = range(len(Gold.index))
    Jungler.index = range(len(Jungler.index))
    Mid.index = range(len(Mid.index))
    Exp.index = range(len(Exp.index))
    Roamer.index = range(len(Roamer.index))