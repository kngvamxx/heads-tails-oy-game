import random

seed_num=int(input("enter any number to create seed\n:"))
random.seed(seed_num)

user_in=input('"heads" or "tails"').lower()

random_choice=random.randint(0,1)

if random_choice==0 and user_in=="heads":
  print("heads you win")
elif random_choice==1 and user_in=="tails":
  print("tails you win")  
else:
  print("you lose")  