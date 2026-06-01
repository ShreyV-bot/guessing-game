ans =False
high =100
low=0
input('Think of anumber between 1 and 100.Please press enter to continue')
guess =0
import random as rn
while not ans:
    print(f'Is you number {guess}')
    resp = input("""Enter 'h' to indicate the guess is too high.
Enter 'l' to indicate the guess is too low.
Enter 'c' to indicate the guess is correct.
Enter Answer: """).lower()
    if resp=='h':
        print('My guess was too hiegh')
        high=guess-1
        guess=rn.randint(low,high)
        ##guess=(high-low)//2 +low
    elif resp=='l':
        print('My guess was too low')
        low=guess+1
        guess=rn.randint(low,high)
        ##guess=(high-low)//2 +low
    elif resp=='c':
        print('Thanks for playing with me!')
        ans=True
