# python-rock-paper-scissors

## Author: Jeffrey Smith

### credit assistants to people from google and Christian-@CDcode

Rock-Paper-scissors is a simple game that people love to play. I created the game in C++ while I was in college a long time ago so I decided to see if I could code it into python. The code below was the start of writing it into Python.

```python
import random
# 1 is paper 2 is scissor 3 is rock
cNumber = [1, 2, 3]
var = input('rock paper or scissor/ type like r/p/s: ').lower()
number = random.choice(cNumber)

user = 0
computer = 0

if var == 'r':

    if number == 1:
        print('you lose')
        computer += 1
    elif number == 2:
        print('you win')
        user += 1
    elif number == 3:
        print('its a tie')
        user += 1
        computer +=1

elif var == 'p':

    if number == 1:
        print('its a tie')
        user += 1
        computer += 1
    elif number == 2:
        print('you lose')
        computer += 1
    elif number == 3:
        print('you won')
        user += 1

elif var == 's':
    
    if number == 1:
        print('you win')
    elif number == 2:
        print('its a tie')
    elif number == 3:
        print('you lose')
        
print(f"ur score {user}")
print(f"comp score {computer}")

```

To the code above I wanted to make it better. I changed it up and improved the code.
