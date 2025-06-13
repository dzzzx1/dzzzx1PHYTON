def party(name):
    n = len(name)
    if n==0:
        print("Никто не пришел на вечеринку")
    elif n==1:
        print( f"На вечеринке {name[0]} ")
    elif n==2:
        print( f"{name[0]} и {name[1]} на вечеринке")
    else:
        print( f"{name[0]}, {name[1]} и {n-2} других на вечеинке")

name = ["Миша", "Ваня", "Юля", "вапр", "апаропорл"]
party(name)