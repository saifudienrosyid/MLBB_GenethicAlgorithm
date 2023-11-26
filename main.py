import matplotlib.pyplot as plt
import random
from geneticalgorithm.Dataset import preprocess_data
from geneticalgorithm.GeneticAlgorithm import genetic_algorithm

# Load and preprocess data
file_path = 'dataset/Mlbb_Heroes.csv'
df, hero_df, total_he, total_tf = preprocess_data(file_path)
hero_data = hero_df.to_dict(orient='records')

# Initialize population
pop_size = 10
population = [random.sample(hero_data[:-1], 5) for _ in range(pop_size)]

# Set algorithm parameters
target_positions = ['Gold Lane', 'Mid', 'EXP Lane', 'Roamer', 'Jungler']
generations = 30
tournament_size = 3
crossover_rate = 0.8
mutation_rate = 0.1

# Run genetic algorithm for hard engage
team_strategy_hard_engage = 0
result_hard_engage, temp_result_hard_engage = genetic_algorithm(population, hero_data, target_positions, generations, tournament_size, crossover_rate, mutation_rate, team_strategy_hard_engage, pop_size)

# Run genetic algorithm for team fight
team_strategy_team_fight = 1
result_team_fight, temp_result_team_fight = genetic_algorithm(population, hero_data, target_positions, generations, tournament_size, crossover_rate, mutation_rate, team_strategy_team_fight, pop_size)

# Print and visualize results
print("Individu Terbaik (Hard Engage):")
for hero in result_hard_engage:
    print(f"Name: {hero['Name']}, Lane: {hero['Lane']}")

print("Individu Terbaik (Team Fight):")
for hero in result_team_fight:
    print(f"Name: {hero['Name']}, Lane: {hero['Lane']}")

# Plot fitness progress for both strategies on the same graph
plt.plot((temp_result_hard_engage / total_he) * 100, label="Hard Engage")
plt.plot((temp_result_team_fight / total_tf) * 100, label="Team Fight")

plt.title("Fitness Progress")
plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.legend()  # Add legend to differentiate the lines
plt.show()

print(result_hard_engage)