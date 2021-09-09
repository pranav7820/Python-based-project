import random

def wingame(you,comp):
    if you==comp:
        return None

    if comp=="s":
        if you=="w":
            return False
        elif you=="g":
            return True 

    if comp=="w":
        if you=="g":
            return False
        elif you=="s":
            return True 

    if comp=="g":
        if you=="s":
            return False
        elif you=="w":
            return True 
    
print("computor turn :snake{s} gun{g} and water{w} ?")

randm=random.randint(1,3)
if randm==1:
    comp="s"
elif randm==2:
    comp="w"
elif randm==3:
    comp="g"
 
you =input("your turn:scissor{s} gun{g} and water{w}?")

pnna=wingame(comp,you)
print(f"comp choose  {comp}")
print(f"you chhose   {you}")

if comp==you:
    print("Game is tie")
elif you:
    print("congrats you win the game") 
elif comp:
    print("you loose the game \n try again")       







    


        