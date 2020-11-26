# delay time
import time
# game begins

# player stats

strength = 0
athleticism = 0
shooting = 0
guard = False
forward = False
center = False

name = str(input("Your name is "))
print()
print("Choose one of the following positions")
print("[1] Guard\n[2] Forward\n[3] Center")
position = input("Enter Choice: ")

if position == "1":
  strength = strength + 5
  athleticism = athleticism + 20
  shooting = shooting + 30
  print("You have chosen to be a Guard")
  guard = True
elif position == "2":
  strength = strength + 20
  athleticism = athleticism + 30
  shooting = shooting + 15
  print("You have chosen to be a Forward")
  forward = True
elif position == "3":
  strength = strength + 40
  athleticism = athleticism + 5
  shooting = shooting + 10
  print("You have chosen to be a Center")
  center = True

print()
print("Your current stats: ")
print(f"Strength: {strength}\nAthleticism: {athleticism}\nShooting: {shooting}")

time.sleep(2)

print()
print("Your adventure begins.....")
print()

time.sleep(2)

print("You are a top High School Basketball Prospect...")
print()
print("You finish your senior season strong and receive the MVP award.")
print("You receive many D1 scholarship offers from many schools. You decide to accept one of these scholarships, rather than going straight to the NBA. You narrow it down between the top 3 school offers.")
print()

# use delay to allow user to read text
time.sleep(6)

# the user must decide which school they're going to (doesn't affect story)
print("You choose:")
print("[1] Kentucky \n[2] Duke \n[3] UCLA")
school = (input("Enter Choice: "))

# use if statements to define varible as words

if school == "1":
    school = "Kentucky"
if school == "2":
    school = "Duke"
if school == "3":
    school = "UCLA"

print()
print(f"You have decided to go to {school}")
# results of choices
print()
time.sleep(1)
print(f"At {school}, you are heading to Basketball practice, when all of a sudden, your friends approach you, asking if you want to come to the party with them.")
print()

# use delay to allow user to read text
time.sleep(3)

print("You decide to:")
# break off into another choice selection
print("[1] Go Party with Friends\n[2] Goto Practice")
choice = input("Enter Choice: ")

# results of choice
if choice == "1":
  if guard == True:
    strength = strength + 0
    athleticism = athleticism + 0
    shooting = shooting - 5
  elif forward == True:
    strength = strength + 0
    athleticism = athleticism - 5
    shooting = shooting + 0
  elif center == True:
    strength = strength - 10
    athleticism = athleticism + 0
    shooting = shooting - 5

  print("\nYou miss out on practice to go party, and you end up playing losing valuable practice time. You keep on partying under the influence of your friends, and you slowly start losing your skill at basketball")

elif choice == "2":
  if guard == True:
    strength = strength + 10
    athleticism = athleticism + 5
    shooting = shooting + 15
  elif forward == True:
    strength = strength + 10
    athleticism = athleticism + 5
    shooting = shooting + 10
  elif center == True:
    strength = strength + 10
    athleticism = athleticism + 15
    shooting = shooting + 5
  print("\nYou tell your friends that you need to goto practice. You practice day and night, improving on your overall skills, becoming a top college Basketball player. You earn the recognition of many people ")
time.sleep(1)

# show user their current stats


print()

time.sleep(2)

print("Updated stats:")

# show the user their stats
if choice == "1":
  if guard == True:
    print(f"Strength: {strength}(+0)\nAthleticism: {athleticism}(+0)\nShooting: {shooting}(-5)")
  elif forward == True:
    print(f"Strength: {strength}(+0)\nAthleticism: {athleticism}(-5)\nShooting: {shooting}(+0)")
  elif center == True:
    print(f"Strength: {strength}(-10)\nAthleticism: {athleticism}(+0)\nShooting: {shooting}(-5)")
elif choice == "2":
  if guard == True:
    print(f"Strength: {strength}(+10)\nAthleticism: {athleticism}(+5)\nShooting: {shooting}(+15)")
  elif forward == True:
    print(f"Strength: {strength}(+10)\nAthleticism: {athleticism}(+5)\nShooting: {shooting}(+10)")
  elif center == True:
    print(f"Strength: {strength}(+10)\nAthleticism: {athleticism}(+15)\nShooting: {shooting}(+5)")

time.sleep(3)

print()
print("You made it to the Finals of the March Madness Final Four. In your final game, your team is up against Kansas State University. You are up against the future Number 1 Draft Pick, Tacko Fell.")

# use delay to allow user to read text
time.sleep(4)

print()
print("You take the last shot.....")
time.sleep(2)

if strength >= 40  or athleticism >= 35 or shooting >= 45:
  print() 
  print(f"You and {school} have beaten Kansas State University and you have won the Finals for March Madness. After beating the future Number 1 Draft Pick Tacko Fell, you get scouted by more teams which increases your Draft pick slot as well.")

# use delay to allow user to read text
  time.sleep(4)

# allow users to choose the team they want to play for (doesn't affect story)
  
  print()
  print("Many eyes are on you now and you must decide which team you want to play for.")

  time.sleep(2)

  print()
  print("Your top 3 choices are:")
  print("[1] Toronto Raptors \n[2] Boston Celtics \n[3] Miami Heat")
  team = input("Choose Team: ")

# use if statements to define varible as words

  if team == "1":
    team = "Toronto Raptors"
  elif team == "2":
    team = "Boston Celtics"
  elif team == "3":
    team = "Miami Heat"

  print()
  print(f"You have selected the {team}.")
  
  time.sleep(2)

  print(f"\nYou get drafted to play with the {team}. \nIn a preseason game, down by 1, with 5 seconds on the clock, the ball is in your hands. You call for an Isolation, but you can also pass it to your teammate.")
  print()

# use delay to allow user to read text
  time.sleep(4)

#break off into choice selection
  print("[1] Go for a Layup \n[2] Go for a Dunk \n[3] Shoot the Ball \n[4] Pass the Ball")
  choice = input("Enter Choice: ")
  print()

# results of choice
  if choice == "1":
    if athleticism >= 30:
      print("You drive in and go for a tough reverse Layup.... ")
      time.sleep(1)
      print()
      print(f"And you score!!! The crowd is yelling {name}!, {name}!, {name}!")
      print("Your team wins the game and now everyone sees you as an amazing player!")
      print("\nYour career only get better from here. You end up winning the playoffs with your team and you become considered one of the best young talents the world has ever seen.")
      print("\nThe End")
    else:
      print("You are unable to make the Layup and you end up costing your team the game.\n\nYou end up on Shaqtin' a Fool.\n\nShaqtin' a Fool is where all careers end. Your career is over")
  elif choice == "2":
    if strength >= 30:
      print("You post up and go for a dunk")
      time.sleep(1)
      print()
      print("You end up posterizing the defender, making a fool out of him! Your play has just made it on ESPN SportCentre's Plays of the Week. After that highlight, you put a name for yourself in the NBA and gained fame.")
      print("\nYour career only get better from here. You end up winning the playoffs with your team and you become considered one of the best young talents the world has ever seen.")
      print("\nThe End")
    else:
      print("You end up missing the dunk, traveling, and now the coach is diappointed and the crowd is laughing at you. \n\nLater, you were put on Shaqtin' a Fool. \n\nShaqtin' a Fool is where all careers end. Your career has ended.")
  elif choice == "3":
    if shooting >= 30:
      print("You scored the three-pointer and take the win home. You buzzer beater has gained the respect of many, and you are now a contender for Rookie of the Year")
      print("\nYour career only get better from here. You end up winning the playoffs with your team and you become considered one of the best young talents the world has ever seen.")
      print("\nThe End")
    else:
      print("You airball the wide open shot because you're not a shooter. Everyone makes fun of you and later, you end up on Shaqtin' a Fool. \n\nShaqtin' a Fool is where all careers end. Your career has ended.")
  elif choice == "4":
    print("\nYour teammate misses the shot. Your coach and the fans think that you lack confidence and that your a no-good player. You start to receive no playing time \n\nYour career slows down drastically. Your adventure ends here")
else:
  print()
  print("You lose to Tacko Fell because your skills are lacking due to all the partying and practices that you miss out on. You sadly remain undrafted for the next draft picking.\n\nYour adventure ends here.")
