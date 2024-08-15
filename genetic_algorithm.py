
import random
import numpy as np

# Параметры алгоритма
C = 100  # Издержки
D0 = 1000  # Базовый уровень спроса
E = 1.5  # Эластичность спроса
P_min = 50  # Минимальная цена
P_max = 200  # Максимальная цена
N = 100  # Размер популяции
p_m = 0.01  # Вероятность мутации
p_c = 0.7  # Вероятность скрещивания
G = 100  # Количество поколений

# Функция оценки прибыли
def calculate_profit(P):
    Q = D0 * P**(-E)
    profit = Q * P - C
    return profit

# Генерация начальной популяции
def generate_population(size, P_min, P_max):
    return [random.uniform(P_min, P_max) for _ in range(size)]

# Функция скрещивания
def crossover(parent1, parent2):
    alpha = random.uniform(0, 1)
    return alpha * parent1 + (1 - alpha) * parent2

# Функция мутации
def mutate(price, P_min, P_max, p_m):
    if random.random() < p_m:
        return random.uniform(P_min, P_max)
    return price

# Основной алгоритм генетического алгоритма
def genetic_algorithm(N, G, P_min, P_max, p_m, p_c):
    # Инициализация популяции
    population = generate_population(N, P_min, P_max)
    
    for generation in range(G):
        # Оценка приспособленности
        fitness_scores = [calculate_profit(P) for P in population]
        
        # Отбор лучших индивидов
        selected_indices = np.argsort(fitness_scores)[-N//2:]
        selected_population = [population[i] for i in selected_indices]
        
        new_population = []
        
        while len(new_population) < N:
            if random.random() < p_c:
                # Скрещивание
                parent1 = random.choice(selected_population)
                parent2 = random.choice(selected_population)
                offspring = crossover(parent1, parent2)
            else:
                # Без скрещивания
                offspring = random.choice(selected_population)
                
            offspring = mutate(offspring, P_min, P_max, p_m)
            new_population.append(offspring)
        
        population = new_population
    
    # Выбор лучшего решения
    best_index = np.argmax([calculate_profit(P) for P in population])
    best_price = population[best_index]
    
    return best_price

optimal_price = genetic_algorithm(N, G, P_min, P_max, p_m, p_c)
print(f"Optimal Price: {optimal_price}")
