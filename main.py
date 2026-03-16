from random import uniform, randint
from os import system

scores = {
    "tech": 1,
    "sports": 1,
    "music": 1,
    "theatre": 1,
    "dogs": 1,
    "politics": 1,
    "film": 1,
    "books": 1,
}

def sum_scores(scores:dict):
    score_sum = 0
    
    for value in scores.values():
        score_sum += value
        
    return score_sum
        
        
def recommend_category(scores):
    total = sum_scores(scores)

    r = randint(0, total)
    
    running_sum = 0
    
    for category, score in scores.items():
        running_sum += score
        
        if r <= running_sum:
            return category
        

def random_category(scores:dict):
    random_number = randint(0, len(scores))
    
    category_names = [key for key, value in scores.items()]
    random_category_name = category_names[random_number-1]
    return random_category_name
    
    
def adjust_weight(scores:dict, category_name:str, score_change:int):
    scores[category_name] += score_change
    
    return scores


def adjust_scores(scores:dict):
    for category, score in scores.items():
        if (score - 1 >= 0): scores[category] = score - 1
        else: scores[category] = 0

    return scores


def save_data_to_file(training_round:int, data:dict):
    with open("output.csv", "a") as out_file:
        output = [f"{value}" for key, value in scores.items()]
        out_file.write(f"{training_round},{','.join(output)}\n")

EXPLORATION_RATE = 0.5
training_round = 0 # Only used to make an index in the CSV file for making a graph in excel
current_is_random = False

while training_round < 1000:
    system("cls")
    print(scores)
    
    random_number = round(uniform(0, 1), 2)

    sum_scores(scores)

    recommended_category:str = ""

    if random_number < EXPLORATION_RATE:
        recommended_category = random_category(scores)
        # print(f"Random category selection: {recommended_category}")
        current_is_random = True
    else:
        recommended_category = recommend_category(scores)
        current_is_random = False
        # print(f"Recommendation: {recommended_category}")

    # print(f"Training round: {training_round}")
    # print(f"Training round % 10 == {training_round % 10}")
    
    # Comment or uncomment one of the two action = lines to match what you want to do, currently it's set up to run x training
    # sets automatically, but with a tiny bit of tweaking you can put it back to how I had it originally, where you had to choose the 
    # action that is performed
    
    # action:int = int(input("Select the action you want to take:\n1: Click\n2: Like\n3:Comment\n4: Ignore\n\n"))
    action = randint(0, 4)
    
    change:int = 0
    
    match action:
        case 1: change = 1
        case 2: change = 3
        case 3: change = 5
        case 4: change = -1
        case _:pass

    if (current_is_random and change == -1): change = -2
        
    adjust_weight(scores, recommended_category, change)
    
    training_round += 1
    save_data_to_file(training_round, scores)

    # Run the adjust scores function every 10 rounds to ensure that things don't become over weighted
    if (training_round % 10 == 0):scores = adjust_scores(scores)

import build_graphics