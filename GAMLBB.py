import numpy as np

def GA_MLBB(dataset, generations, init_pop):
    population = initialize_population(init_pop, 5)
    fit_value = []
    for individual in population:
        a= fitness_starg1(individual)
        fit_value.append(a)
    fit_value

    #select parent
    parents= selection(4,fit_value,population)
    child=crossover_4_parents(parents[1], parents[2], parents[3], parents[4])

    #add child ke population
    population.extend(child)
    wr_value = []
    for individual in population:
        a= func_mutation(individual)
        wr_value.append(a)
    
    #hasil mutasi
    mutation_result= [value for value in wr_value if value > 0.50]

    new_pop= []
    index =[]
    for i in mutation_result:
        ind = wr_value.index(i)
        index.append(ind)
    
    for i in index:
        new_pop.append(population[i])

    return new_pop

#fitness Function
def fitness_starg1(df,team):
    ind1=0
    ind2=0
    for h in team:
        ind1 += df['Hard_Engage'][h]
        ind2 += df['Win_Rate'][h]
    fit = ind1 * (ind2/5)
    return fit

#Init population
import random
def generate_individual(chromosome_length):
    def random_integer_except(excluded_value):
        while True:
            random_value = random.randint(44, 94)  # Ganti rentang sesuai kebutuhan Anda
            if random_value != excluded_value:
                return random_value
    # Fungsi ini menghasilkan satu individu acak dengan panjang kromosom tertentu.
    individual= [0]*chromosome_length
    individual[0] = random.randint(1,18)
    individual[1] = random.randint(19,43)
    individual[2] = random.randint(44,76)
    individual[3] = random.randint(77,101)
    individual[4] = random.choice([random_integer_except([individual[2],individual[3]]), random.randint(102,114)])

    return individual

def initialize_population(population_size, chromosome_length):
    # Fungsi ini menghasilkan populasi awal dengan sejumlah individu.
    return [generate_individual(chromosome_length) for _ in range(population_size)]

#selection
import heapq
def selection(num_select, population, fit_value,):
    fit_selected = heapq.nlargest(num_select,fit_value)
    parents1= population[fit_value.index(fit_selected[0])]
    parents2= population[fit_value.index(fit_selected[1])]
    parents3= population[fit_value.index(fit_selected[2])]
    parents4= population[fit_value.index(fit_selected[3])]
    parents= [parents1, parents2, parents3, parents4]
    return parents

#cross-over
def crossover_4_parents(parent1, parent2, parent3, parent4):
    # Menghitung panjang kromosom
    chromosome_length = len(parent1)

    # Memilih dua titik crossover acak
    crossover_point1 = random.randint(1, chromosome_length - 1)
    crossover_point2 = random.randint(1, chromosome_length - 1)

    # Memastikan titik crossover1 dan crossover2 berbeda
    while crossover_point1 == crossover_point2:
        crossover_point2 = random.randint(1, chromosome_length - 1)

    # Mengurutkan titik crossover
    crossover_point1, crossover_point2 = min(crossover_point1, crossover_point2), max(crossover_point1, crossover_point2)

    # Membuat empat anak baru dengan menggabungkan gen dari empat orangtua
    child1 = parent1[:crossover_point1] + parent2[crossover_point1:crossover_point2] + parent3[crossover_point2:] + parent4[crossover_point2:]
    child2 = parent3[:crossover_point1] + parent4[crossover_point1:crossover_point2] + parent1[crossover_point2:] + parent2[crossover_point2:]
    child3 = parent2[:crossover_point1] + parent1[crossover_point1:crossover_point2] + parent4[crossover_point2:] + parent3[crossover_point2:]
    child4 = parent4[:crossover_point1] + parent3[crossover_point1:crossover_point2] + parent2[crossover_point2:] + parent1[crossover_point2:]

    child=[child1, child2, child3, child4]
    return child

#num_parents_mating

#parent_selection_type

#keep_parents

#mutation_function
def func_mutation(team):
    wr=0
    for h in team:
        wr += df['Win_Rate'][h]

    wr = wr/5
    return wr
#mutation_percent_gens

