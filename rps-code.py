import os
import random
def cls():
    os.system('cls')
cls()
def rock():print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

def paper(): 
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')

def scissors():
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

print("ROCK, PAPER and SCISSORS")
print("type 1 for rock 2 for paper and 3 for scissors")
ans = int(input())
cans = random.randint(1,3)
if ans == 1:
    rock()
elif ans == 2:
    paper()
elif ans == 3:
    scissors()
print("\nComputer chose: \n")
if cans == 1:
    rock()
elif cans == 2:
    paper()
elif cans == 3:
    scissors()
global ft
if ans == 1 and cans == 3:
    ft = 1
if ans == 1 and cans == 2:
    ft = 0
if ans == 2 and cans == 3:
   ft = 0
if ans == 2 and cans == 1:
    ft = 1
if ans == 3 and cans == 2:
    ft = 1
if ans == 3 and cans == 1:
    ft = 0
if (ans == 1 and cans ==1) or (ans == 2 and cans == 2) or (ans == 3 and cans == 3):
    ft = 3
if ft == 1:
    print("\nYOU WIN")
elif ft == 3:
    print("\nTIE")
else:
    print("\nYOU LOOSE")


