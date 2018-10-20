#Kyla Ryan
#10/18

#start
print("Your plane has landed after a tiring trip taking literally hours.\n"
      "The landing was a bit rough, but you were landing on the beach. A\n"
      "calm breeze moved through the sands to wake up the waves. It was \n"
      "enjoyable. You needed some time for yourself, so you go towards  \n"
      "the water.")
#INPUT_WATER HERE***
in_water_app=["A","a","b","B"]
input_water=input("You have one of two options:\n"
                  "A. Walk along the beach.\n"
                  "B. Look around.\n"
                  "")

if input_water=="A" or input_water=="a":
    print("You walked along the beach, not taking ten steps before\n"
          "stepping on something hard.")
elif input_water=="B" or input_water=="b":
    print("You look around the water, enjoying the breeze before  \n"
          "your eyes catch something in the water.")
else:
    while input_water!=in_water_app:
            input_water=input("You have one of two options:\n"
                              "A. Walk along the beach.\n"
                              "B. Look around.\n"
                              "")
            if input_water=="A" or input_water=="a":
                print("You walked along the beach, not taking ten steps before\n"
                      "stepping on something hard.")
            elif input_water=="B" or input_water=="b":

                print("You look around the water, enjoying the breeze before  \n"
                      "your eyes catch something in the water.")
        
#INPUT_RUNE HERE***
if input_water=="a" or input_water=="A":
    in_rune_app=["A","a","B","b"]
    input_rune=input("You have one of two options:\n"
                     "A. Just a rock.\n"
                     "B. Pick it up.\n"
                     "")
    
    if input_rune=="a" or input_rune=="A":
        print("You continue walking, thinking it is just a rock.\n"
              "There is nothing else to do here.")
    elif input_rune=="b" or input_rune=="B":
        print("You pick up the rock, finding that it is a rune  \n"
              "with beautiful engravings. You continue walking  \n"
              "but find there is nothing else to do.")
    else:
        while input_rune!=in_rune_app:
            input_rune=input("You have one of two options:\n"
                              "A. Just a rock.\n"
                              "B. Pick it up.\n"
                              "")
            if input_rune=="a" or input_rune=="A":
                print("You continue walking, thinking it is just a rock.\n"
                      "There is nothing else to do here.")
            elif input_rune=="b" or input_rune=="B":
                print("You pick up the rock, finding that it is a rune  \n"
                      "with beautiful engravings. You continue walking  \n"
                      "but find there is nothing else to do.")
#INPUT_SHELL HERE***
if input_water=="b" or input_water=="B":
    in_shell_app=["a","A","B","b"]
    input_shell=input("You have one of two options:\n"
                      "A. Probably just a shell.\n"
                      "B. Pick it up.\n"
                      "")
    if input_shell=="a" or input_shell=="A":
        print("You continue looking at the ocean, feeling refreshed.\n"
              "You find there is nothing else here.")
    elif input_shell=="b" or input_shell=="B":
        print("You pick it up, finding that it was just a shell. You\n"
              "find that there is nothing else here.")
    else:
        while input_shell!=in_shell_app:
            input_shell=input("You have one of two options:\n"
                              "A. Probably just a shell.\n"
                              "B. Pick it up.\n"
                              "")
            if input_shell=="a" or input_shell=="A":
                print("You continue looking at the ocean, feeling refreshed.\n"
                      "You find there is nothing else here.")
            elif input_shell=="b" or input_shell=="B":
                print("You pick it up, finding that it was just a shell. You\n"
                      "find that there is nothing else here.")
        
#HANGAR INPUT HERE***
if input_rune=="a" or input_rune=="A" or input_rune=="b" or input_rune=="B" or input_shell=="a" or input_shell=="A" or input_shell=="B" or input_shell=="b":
    hangar=input("Do you want to go to the Plane Hangar? ")
    if hangar=="y" or hangar=="Y":
        print("You walked inside to the Plane Hangar. You've been here before, \n"
              "and knew where you were going. There were many new faces about.")
    else:
        print("There's nothing to do here. The only other place you can go is  \n"
              "the Plane Hangar.")


