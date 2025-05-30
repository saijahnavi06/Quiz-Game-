print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay ! Let's play :)") 
   
answer =input("what does CPU stand for? ")
if answer == "Central processing unit":
    print('correct!')
else:
    print("Incorrect!") 
answer =input(" what does GPU stand for? ")
if answer == "graphics processing unit":
    print('correct!')
else:
    print("Incorrect!")
answer =input("what does RAM stand for? ")
if answer == "random access memory":
    print('correct!')
else:
    print("Incorrect!")
answer =input("what does PSU stand for? ")
if answer == "power supply ":
    print('correct!')
else:
    print("Incorrect!")