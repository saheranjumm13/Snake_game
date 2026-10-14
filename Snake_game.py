'''
    1 for snake 
    -1 for water
    0 for gun
'''

computer=random.choice[-1,0,1]
com=input("Enter your choice:")
dict={"s":1, "w":-1, "g":0}
revdict={1:"Snake", 2:"Water", 3:"Gun"}
choice=dict[com]
print(f"You chose {revdict[choice]}\n Computer Chose{revdict[computer]}")

if(computer==choice):
    print("Draw")
else:
    if(computer==-1 and choice==1):
        print("You win")
    elif(computer==-1 and choice==0):
        print("You Lose")
    elif(computer==1 and choice==-1):
        print("You Lose")
    elif(computer==1 and choice==0):
        print("You Win")
    elif(computer==0 and choice==-1):
        print("You Win")
    elif(computer==0 and choice==1):
        print("You Lose")

    else:
        print("Something went wrong")