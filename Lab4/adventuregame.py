answer = input("Do you want to try this adventure game? [yes/no] ")
if answer == "no":
 answer = input("Alright, maybe another time.")
elif answer == "yes":
    print("Let's begin!")
print()
answer = input("While searching for your missing friend, you reach a place where many kids have vanished Ahead of you are two options: eerie woods, or the old Trum family house where a massacre happened. Your friend loved thrills. Where do you go? [Woods/House]")

if answer == "House":
    answer = input("Do you want to step inside the house? [yes/no] ")
if answer == "yes":
    print()
print("Inside, you notice another door that looks like it was opened recently.")
if answer == "no":
    print("You decide to leave. You survive.")
print()
answer = input("Do you want to walk through the creaking door? [yes/no] ")
if answer == "yes":
    print()
answer = input()
"You open the door and see complete darkness. As you walk forward, you hear a noise to your left. "
"Do you explore the room or follow the noise? [Explore/Follow the Noise] "

if answer == "Explore":
        print()
answer = input()
"While exploring, you find a broken lever near a bed, covered in splinters. "
"Do you pull the lever? [yes/no] "

if answer == "yes":


    print()
    
answer = input("The lever moves and a gate opens. You hear your friend's voice and walk forward until"
"everything goes pitch black. Do you turn back? [yes/no] ")


if answer == "no":
   print("You have died.")
if answer == "yes":
    print()
"You turn around, realizing this was a mistake. Before you can escape, a long tendril-like " 
"arm pulls you back inside. YOU LOSE!"
if answer == "Follow the Noise":
    print("The sound leads you into a trap. Something grabs you from behind. YOU LOSE!")
    if answer == "no":
        print("You leave the house safely, but your friend is never found. THE END.")
print()
print("The house is empty, dusty, and silent. You feel like you're being watched.")
if answer == "Woods":
    print()
answer = input()
"The temperature drops as you enter the woods. A monster appears and stares at you. "
"Do you run? [Yes/No] "

if answer == "Yes":
    print()
"You run as fast as you can. A car passes by and you scream for help, "
"but the monster catches you and devours you. YOU LOSE!"

print()
if answer == "No":
    print("You stand still. After a tense moment, the monster turns away and disappears. YOU SURVIVE!")