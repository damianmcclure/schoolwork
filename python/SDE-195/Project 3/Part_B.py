import pyautogui
import random
import string

# function that grabs mouse position and creates a truly random seed
def random_from_mouse():
    pos = pyautogui.position()
    sd = pos[0]+1j*pos[1]
    random.seed(sd)
    return random.random()

# User inputs to have the user move the mouse 3 times
input("This program will generate a *true* random password using your mouse inputs. Presse enter to start.")
seed1 = random_from_mouse()
input("Move the mouse to a new location, and press enter.")
seed2 = random_from_mouse()
input("Move the mouse to another new location, and press enter.")
seed3 = random_from_mouse()

# Times the 3 seeds together to make one seed
finalseed = seed1*seed2*seed3

# Length input
length = int(input("Enter length of password you want: "))

# Generating the random password with the seed
chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = finalseed
password = ''.join(random.choice(chars) for i in range(length))

# Printing the password created
print(password)
