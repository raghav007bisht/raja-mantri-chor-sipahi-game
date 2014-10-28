import random
import time
print('##############################################################')
time.sleep(2)
print('#                  Raja Mantri Chor Sipahi                   #')
time.sleep(2)
print('#                                Programmer : Raghav Bisht   #')
time.sleep(2)
print('##############################################################')
print()
print('************************************')
print('*          Rules...!!              *')
print('************************************')
print('It is a simple game in which you have to guess the...')
print('who is chor & sipahi if you are mantri...')
print('If you are sipahi you will get 100 points...')
print('If you are chor you will get 00 points...')
print('If you are mantri & your guess is correct you will get 150 points...')
print('If you are king you will get 200 points...')
print()
print('##############################################################')
print()

PScore=0
CScore=0
count = 0
while (count < 3):
    print('Starting Game Wait For A Sec...')
    time.sleep(5)
    royal = ['raja', 'mantri']
    people = ['chor','sipahi']

    chooseRoyal = random.choice(royal)

    if chooseRoyal.lower() == 'raja':
        time.sleep(2)
        print('Congrats You Are Raja')
        time.sleep(2)
        print('Congrats You Get 200 Points')
        PScore=PScore+200
    
    elif chooseRoyal.lower() == 'mantri':
        time.sleep(2)
        print('Congrats You Are Mantri')
        time.sleep(2)
        print()
        print('On Raja Command Find Who Is CHOR & SIPAHI')
        guess = input('Who am I chor or sipahi :')
        choosePeople = random.choice(people)
        if guess.lower() == choosePeople:
              time.sleep(2)
              print('You are correct..')
              time.sleep(2)
              print('he is ',choosePeople)
              PScore=PScore+150
        if guess.lower() != choosePeople:
              time.sleep(2)
              print('You are worng..')
              time.sleep(2)
              print('he is ',choosePeople)
              CScore=CScore+150
    print()
    input('Press Enter to start again....')
    print()
    print(30*'*')
    count = count + 1
    
print('total Player Score is =',PScore)
print('total Computer Score is =',CScore)
if (PScore > CScore):
    print('Player Win...!!!!!!!')
elif (CScore > PScore):
    print('Computer Win...!!!!!')
elif (PScore == CScore):
    print('Both Score Are Equal So, Player Win')
