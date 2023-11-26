import pandas as pd

def preprocess_data(file_path):
    df = pd.read_csv(file_path)
    df['Hero_Defense'] = df['Mag_Defence'] + df['Phy_Defence']
    df['Win_Rate'] = df['Esport_Wins'] / (df['Esport_Wins'] + df['Esport_Loss'])
    df['Hard_Engage'] = (df['Phy_Damage'] + df['Mov_Speed'])
    df['Team_Fight'] = (df['Phy_Damage'] + df['Hp'] + df['Hero_Defense'])
    hero_df = df[['Name', 'Lane', 'Hard_Engage', 'Team_Fight', 'Win_Rate']]

    gold = df[df['Lane'] == 'Gold Lane']
    mid = df[df['Lane'] == 'Mid']
    exp = df[df['Lane'] == 'EXP Lane']
    roamer = df[df['Lane'] == 'Roamer']
    jungler = df[df['Lane'] == 'Jungler']
    # Create a list of dataframes for each role
    roles = [gold, mid, exp, roamer, jungler]

    # Calculate the sum of (Hard_Engage * Win_Rate) and (Team_Fight * Win_Rate) for each role
    max_hard_engage_sums = [role.groupby('Lane').apply(lambda x: (x['Hard_Engage'] * x['Win_Rate']).max()).sum() for role in roles]
    max_team_fight_sums = [role.groupby('Lane').apply(lambda x: (x['Team_Fight'] * x['Win_Rate']).max()).sum() for role in roles]

    # Create a DataFrame to display the results
    result_df = pd.DataFrame({
        'Role': ['Gold Lane', 'Mid', 'EXP Lane', 'Roamer', 'Jungler'],
        'Max_Hard_Engage_Sum': max_hard_engage_sums,
        'Max_Team_Fight_Sum': max_team_fight_sums
    })

    # Calculate the total sum of (Hard_Engage * Win_Rate) and (Team_Fight * Win_Rate)
    total_he = result_df['Max_Hard_Engage_Sum'].sum()
    total_tf = result_df['Max_Team_Fight_Sum'].sum()
    return df, hero_df, total_he, total_tf
