import random
while True:
    todos =["epistemologia", "francuski", "metodologia", "projektowanie maszyn modułowych"]
    los= random.choice(todos)
    print("Czas zabrać się za:", los)
    print("Zrobione? T czy N?")
    done=input()
    if done=="N" or done=="n":
        print("To rusz się do roboty!")
        done=input()
    elif done=="T" or done=="t":
        print("Usuwam", los, "z listy do zrobienia!")
        todos.remove(los)
