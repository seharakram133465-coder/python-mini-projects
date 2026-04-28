

import random
item_list=['rock','paper','scissor']

user_choice= input('enter your choice = rock ,paper , scissore =')
comp_choice=random.choice(item_list)

print(f"user_choice={user_choice} , comp_choice={comp_choice}")

if user_choice == comp_choice:
  print('both choose same = match tie')
  
elif user_choice == 'rock':
  if comp_choice == 'paper':
    print('paper cover rock = computer win')
  else:
    print('rock smashes scissore = you win')



elif user_choice == 'paper':
  if comp_choice == 'scissore':
    print('scissor cut a paper = computer win')
  else:
    print('paper cover rock = you win')


elif user_choice == 'scissore':
  if comp_choice == 'paper':
    print('scissor cut a paper = you win')
  else:
    print('rock smashes scissore = coputer win')


