from dataset import Dataset

max_fit_value = 1


#define wr per hero
def calculate_winrate_by_champion(idChampion, lane):
    winrate = Dataset.df[(Dataset.df['Id'] == idChampion) & (
        Dataset.df['Lane'] == lane)].Win_Rate.values[0]

    return winrate

def fit_function_tim(Tim):
    fitness = 0
    hasCarry = False
    hasSupp = False
    hasMid = False
    hasTop = False
    hasJungle = False
    winrateTop = 0
    winrateJungle = 0
    winrateMid = 0
    winrateCarry = 0
    winrateSupp = 0

    for hero in Tim:
        lanes = Dataset.df.loc[Dataset.df.Id == hero].Lane.to_string()
        if (not hasTop and 'Gold Lane' in lanes):
            hasTop = True
            topInfos = Dataset.df[(Dataset.df['Id'] == hero) & (
                Dataset.df['Lane'] == 'Gold Lane')]
            winrateTop = topInfos.Win_Rate.values[0]
            continue

        if (not hasJungle and 'Jungler' in lanes):
            hasJungle = True
            jungleInfos = Dataset.df[(Dataset.df['Id'] == hero) & (
                Dataset.df['Lane'] == 'Jungler')]
            winrateJungle = jungleInfos.Win_Rate.values[0]
            continue

        if (not hasMid and 'Mid' in lanes):
            hasMid = True
            midInfos = Dataset.df[(Dataset.df['Id'] == hero) & (
                Dataset.df['Lane'] == 'Mid')]
            winrateMid = midInfos.Win_Rate.values[0]
            continue

        if (not hasCarry and 'EXP Lane' in lanes):
            hasCarry = True
            carryInfos = Dataset.df[(Dataset.df['Id'] == hero) & (
                Dataset.df['Lane'] == 'EXP Lane')]
            winrateCarry = carryInfos.Win_Rate.values[0]
            continue

        if (not hasSupp and 'Roamer' in lanes):
            hasSupp = True
            suppInfos = Dataset.df[(Dataset.df['Id'] == hero) & (
                Dataset.df['Lane'] == 'Roamer')]
            winrateSupp = suppInfos.Win_Rate.values[0]
            continue

    #fITNESS
    fitness = (winrateCarry + winrateSupp + winrateMid + winrateTop + winrateJungle)

    return fitness