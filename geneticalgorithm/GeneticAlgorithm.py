import random
import numpy as np
# from app.geneticalgorithm.Dataset import preprocess_data

def calculate_fitness(individual, target_positions, team_strategy):
    fitness_value = 0
    for hero, target_lane in zip(individual, target_positions):
        if hero['Lane'] == target_lane:
            if(team_strategy == 1):
                fitness_value += hero['Team_Fight'] * hero['Win_Rate']
            elif(team_strategy == 0):
                fitness_value += hero['Hard_Engage'] * hero['Win_Rate']
    return fitness_value

def tournament_selection(population, fitness_values, tournament_size):
    selected_parents = []
    for _ in range(len(population)):
        tournament_candidates_indices = random.sample(range(len(population)), tournament_size)
        tournament_candidates_fitness = [fitness_values[i] for i in tournament_candidates_indices]
        winner_index = tournament_candidates_indices[np.argmax(tournament_candidates_fitness)]
        selected_parents.append(population[winner_index])
    return selected_parents

def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(individual, hero_data, mutation_rate):
    for i in range(len(individual)):
        if random.uniform(0, 1) < mutation_rate:
            new_hero = random.choice(hero_data)
            individual[i] = new_hero
    return individual

def genetic_algorithm(population, hero_data, target_positions, generations, tournament_size, crossover_rate, mutation_rate, team_strategy, pop_size):
    temp_result = []
    for generation in range(generations):
        fitness_values = [calculate_fitness(individual, target_positions, team_strategy) for individual in population]
        
        # Seleksi orangtua menggunakan turnamen
        parents = tournament_selection(population, fitness_values, tournament_size)
        
        # Crossover
        children = []
        for i in range(0, len(parents), 2):
            parent1 = parents[i]
            parent2 = parents[i + 1]
            if random.uniform(0, 1) < crossover_rate:
                child1, child2 = crossover(parent1, parent2)
                children.append(child1)
                children.append(child2)
            else:
                children.append(parent1)
                children.append(parent2)
        
        # Mutasi
        mutated_children = [mutate(child, hero_data, mutation_rate) for child in children]
        
        # Gabungkan populasi lama dan baru, lalu pilih individu terbaik
        combined_population = population + mutated_children
        fitness_values_combined = [calculate_fitness(individual, target_positions, team_strategy) for individual in combined_population]
        best_indices_combined = np.argsort(fitness_values_combined)[-pop_size:]
        population = [combined_population[i] for i in best_indices_combined]
        
        # Cetak hasil setiap generasi
        temp_result.append(max(fitness_values))
        print(f"Generasi {generation + 1}, Fitness Terbaik: {max(fitness_values)}")

    # Pilih individu terbaik dari populasi terakhir
    fitness_values = [calculate_fitness(individual, target_positions, team_strategy) for individual in population]
    best_individual_index = np.argmax(fitness_values)
    best_individual = population[best_individual_index]

    return best_individual, temp_result
