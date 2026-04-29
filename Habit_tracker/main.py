from brain import *


print('\n✿———————HABIT TRACKER———————✿')
print(
    '''
    ✿——————————————————————✿
    │          MENU         │
    │   1. View Habits      │
    │   2. Add Habits       │
    │   3. Check Stats      │
    │   4. How to select?   │
    │   5. Exit             │
    ✿——————————————————————✿
    '''
)

choice = input('Please enter your choice (1/2/3/4): ')
all_habits = get_habits()

if choice == '1':
    print('✿———————HABIT LIST————————✿')
    for i in all_habits:
        print(i)
    habit_choice = input('Please enter habit as a number: ')
    for i in all_habits:
        if i.split('.')[0] == habit_choice:
            raw_habit = i
            habit_num = all_habits.index(i) + 1
            habit_selected = i.split('.')[1]
            print(f'✿———————HABIT: {habit_selected}————————✿')
            print('''
    ✿——————————————————————✿
    │          MENU         │
    │   1. Edit Habit       │
    │   2. Delete Habit     │
    │   3. Check Stats      │
    │   4. Back             │
    ✿——————————————————————✿
            ''')
            option = input('Please enter your choice: ')
            if option == '1':
                print(f'✿———————HABIT: {habit_selected}————————✿')
                print('''
    ✿——————————————————————✿
    │          MENU         │
    │   1. Change habit name│
    │   2. Mark as complete │
    │   3. Back             │
    ✿——————————————————————✿
                            ''')
                option = input('Please enter your choice: ')
                if option == '1':
                    print(f'✿———————HABIT: {habit_selected}————————✿')
                    habit_new_name = input('Please enter new habit name: ').capitalize()
                    all_habits.remove(raw_habit)
                    all_habits.append(habit_new_name)
                    print('Habit name updated!')



save_habits(all_habits)