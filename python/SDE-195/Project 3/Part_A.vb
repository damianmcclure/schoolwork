# This is pseudocode
Import pyautogui
Import random
Import string

Function random_from_mouse()
    Define pos as Integer
    pos = pyautogui.position()
    Defien sd as Integer
    sd = pos[0]+1j*pos[1]
    random.seed(sd)
    return random.random()
End Function

Input("This program will generate a *true* random password using your mouse inputs. Presse enter to start.")
Define seed1 as Integer
seed1 = random_from_mouse()
input("Move the mouse to a new location, and press enter.")
Define seed2 as Integer
seed2 = random_from_mouse()
input("Move the mouse to another new location, and press enter.")
Define seed3 as Integer
seed3 = random_from_mouse()

Define finalseed as Integer
finalseed = seed1*seed2*seed3

Define length as Integer
length = int(input("Enter length of password you want: "))
Define chars as String
chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = finalseed

Define password as String
password = ''.join(random.choice(chars) for i in range(length))
print(password)
