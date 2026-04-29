


def get_habits():
    with open('habits.txt', 'r') as f:
        all_habits = f.readlines()
        all_habits = [f'{i+1}.{all_habits[i].strip().capitalize()}' for i in range(len(all_habits))]
        return all_habits


def save_habits(all_habits):
    with open('habits.txt', 'w') as f:
        for habit in all_habits:
            try:
                f.write(habit.split('.')[1] + '\n')
            except IndexError:
                f.write(habit + '\n')