from brain import *
from menus import *


print('\n✿———————HABIT TRACKER———————✿')
print(menus['Main_menu'])

choice = input('Please enter your choice (1/2/3/4): ')
all_habits = get_habits()

if choice == '1':
    print('\n✿———————HABIT LIST————————✿')
    for i in all_habits:
        print(i)
    habit_choice = input('Please enter habit as a number: ')
    for i in all_habits:
        if i.split('.')[0] == habit_choice:
            raw_habit = i
            habit_num = all_habits.index(i) + 1
            habit_selected = i.split('.')[1]
            print(f'\n✿———————HABIT: {habit_selected}————————✿')
            print(menus['Habit_list_menu'])
            option = input('Please enter your choice: ')
            if option == '1':
                print(f'\n✿———————HABIT: {habit_selected}————————✿')
                print(menus["Habit_edit_menu"])
                option = input('Please enter your choice: ')
                if option == '1':
                    print(f'✿———————HABIT: {habit_selected}————————✿')
                    all_habits, habit_selected = update_habit_name(all_habits, raw_habit)
                    print(f'\n✿———————HABIT: {habit_selected}————————✿')
                    print(menus["Habit_edit_menu"])


save_habits(all_habits)