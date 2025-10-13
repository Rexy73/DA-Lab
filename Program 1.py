import random 
num_trials = int(input("Enter_no_of_trials: ")) #2
rolls_per_trial =int(input("For Each trail how many rolls: ")) #5
roll_up_value=int(input("Enter rollup value: ")) #6
poss_outcomes=0 
for i in range(num_trials):
    for j in range(rolls_per_trial):
        result = random.randint(1,6)
        print(result)
        if result == roll_up_value:
            poss_outcomes += 1
    print("--------")
total_outcomes = num_trials * rolls_per_trial 
print(f"Number of times 6 appeared in {num_trials} trials of {rolls_per_trial} rolls each:{poss_outcomes}") 
print("Probability=",poss_outcomes / total_outcomes)
