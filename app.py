# streamlit_app.py
import streamlit as st
import random
from geneticalgorithm.Dataset import preprocess_data
from geneticalgorithm.GeneticAlgorithm import genetic_algorithm
import pandas as pd

st.set_page_config(
    page_title="MLBB GA Concat Boys",
    page_icon="🧊",
    layout="centered", 
    )

file_path = 'dataset/Mlbb_Heroes.csv'
df, hero_df, total_he, total_tf = preprocess_data(file_path)
hero_data = hero_df.to_dict(orient='records')

st.title('Genetic Algorithm MLBB Team Composition')
st.write('Presented by Concat Boys')

st.subheader('Dataframe')
st.dataframe(df[['Name', 'Lane','Hp', 'Phy_Damage', 'Hero_Defense', 'Mov_Speed', 'Hard_Engage', 'Team_Fight', 'Win_Rate']], use_container_width=True)

# Set algorithm parameters
target_positions = st.multiselect(
    'Masukan Target Susunan Pemain',
    ['Gold Lane', 'Mid', 'EXP Lane', 'Roamer', 'Jungler'],
    ['Gold Lane', 'Mid', 'EXP Lane', 'Roamer', 'Jungler']
    )


# Initialize input
pop_size = st.number_input('Ukuran Populasi', min_value=1, value=10)
population = [random.sample(hero_data[:-1], 5) for _ in range(pop_size)]

generations = st.number_input('Jumlah Generasi', min_value=1, value=30)
tournament_size = st.number_input('Tournament Size', min_value=1, value=3, max_value=10)
crossover_rate = st.number_input('Crossover Rate', value=0.8, max_value=1.00)
mutation_rate = st.number_input('Mutation Rate', value=0.10, max_value=1.00)

# Run genetic algorithm for hard engage
team_strategy_hard_engage = 0
result_hard_engage, temp_result_hard_engage = genetic_algorithm(population, hero_data, target_positions, generations, tournament_size, crossover_rate, mutation_rate, team_strategy_hard_engage, pop_size)

# Run genetic algorithm for team fight
team_strategy_team_fight = 1
result_team_fight, temp_result_team_fight = genetic_algorithm(population, hero_data, target_positions, generations, tournament_size, crossover_rate, mutation_rate, team_strategy_team_fight, pop_size)

chart_data = pd.DataFrame({
    "Generations": list(range(1, len(temp_result_hard_engage)+1)),
    "Hard Engage": (temp_result_hard_engage / total_he) * 100,
    "Team Fight": (temp_result_team_fight / total_tf) * 100
})

st.subheader('Fitness Value')
st.line_chart(chart_data, x='Generations', y=["Hard Engage", "Team Fight"], color=["#dc143c", "#a5d805"], width=0, height=0, use_container_width=True)

col1, col2 = st.columns(2)
with col1:
    st.subheader("Hard Engage Strategy:")
    hard_engage_df = pd.DataFrame.from_dict(result_hard_engage)
    st.dataframe(hard_engage_df)
    fitness_tf = ((temp_result_hard_engage[-1] / total_he) * 100)
    st.write(f"Fitness: {fitness_tf:.2f}%")

with col2:
    st.subheader("Team Fight Strategy:")
    team_fight_df = pd.DataFrame.from_dict(result_team_fight)
    st.dataframe(team_fight_df)
    fitness_tf = ((temp_result_team_fight[-1] / total_tf) * 100)
    st.write(f"Fitness: {fitness_tf:.2f}%")