import random

def MontyHallGame():
    # three possible prizes
    objs  = ["Goat","Goat","Ferrari"]
    doors = []

    # fill each door
    for i in range(3):
        index=random.randint(0,len(objs)-1)
        doors+= [objs.pop(index)]

    # pick 1 out of the 3 doors
    first_pick = random.randint(1,3)


    # Show the other dooor with goat
    index=doors.index("Ferrari")
    goat_door = random.choice([i for i in  [1,2,3] if i!=(index+1) and (i!=first_pick)])
    # print(f"There is a goat behind Door {goat_door}")
    user_choice = "Y"
    if(user_choice=="Y"):
        first_pick = random.choice([i for i in  [1,2,3] if i!=(goat_door) and i!=[first_pick]])
    if(doors[first_pick-1]!="Ferrari"):
        # print("You picked a Goat!")
        return False
    # print("Well done you got a ferrari")
    return True

if __name__=="__main__":
    count =0
    ferraris_won =0
    for i in range(0, 1_000_000):
        if(MontyHallGame() == True):
            ferraris_won+=1
        count+=1
    print(f"Won ferrari ({ferraris_won/count}) times")