import random
while True:
    todos =["epi tekst", "francuski dialog", "meto", "epi wykłady"]
    los= random.choice(todos)
    print("Czas zabrać się za:", los)
    print("Zrobione? T czy N?")
    done=input()
    if done=="N":
        print("To rusz dupę")
        done=input()
    elif done=="T":
        print("Usuwam", los, "z listy do zrobienia!")
        todos.remove(los)
