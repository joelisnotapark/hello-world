# delay time
import time
# game begins
name = str(input("Your name is "))

print("Your adventure begins.....")
print()

time.sleep(2)

print("You are a top High School Basketball Prospect...")
print()
print("You finish your senior season strong and receive the MVP award")
print("With the pressure of many people, you have to decide whether you goto college or straight to the NBA")
print()

# use delay to allow user to read text
time.sleep(4)

# the user must decide whether to goto college or straight to the NBA
print("[1] Goto College\n[2] Goto the NBA")
choice = input("Enter Choice: ")

# results of choices
if choice == "1":
  print("\nYou go college to practice and gain more experience \nWhile going to practice, your friends approach you, asking you if you want to a party.")

  # use delay to allow user to read text
  time.sleep(4)

  print()
  # break off into another choice selection
  print("[1] Go Party with Friends\n[2] Goto Practice")
  choice = input("Enter Choice: ")

  # results of choice
  if choice == "1":
    print("\nYou miss out on practice to go party, and you end up playing bad and you lose playing time during your college season. \n\nYou don't end up making the NBA. Your adventure ends here")
  elif choice == "2":
    print("\nYou tell your friends that you need to goto practice. You practice day and night, improving on your skills. You make it to the NBA as a top, well-known Rookie.\n\nIn your first NBA season, as a player, you decide to")
    print()

    # use delay to allow user to read text
    time.sleep(4)

    # break off into another choice selection
    print("[1] Ballhog and Do Everything Yourself\n[2] Set up your teammates to score points")
    choice = input("Enter Choice: ")

    # results of choice
    if choice == "1":
      print("\nEveryone sees you as a ballhog, and a no-good player. You end up losing your status in the NBA and you don't get anymore playing time\n\nYou are no longer the player people once saw you as, Your adventure ends here.")
    elif choice == "2":
      print("\nEveryone in the NBA sees the value of you. The fans also enjoy watching you play. With this play style you end up winning the championship and win the MVP award.\n\nCongrats, You have made it to the top and you are now considered one of the best!")
    
elif choice == "2":
  print("\nYou get drafted to the NBA, but without popularity. \nIn a preseason game, down by 1, with 5 seconds on the clock, the ball is in your hands. You have and open shot, but you can also pass it to your teammate.")
  print()

  # use delay to allow user to read text
  time.sleep(4)

  #break off into choice selection
  print("[1] Pass the Ball\n[2] Shoot the Ball")
  choice = input("Enter Choice: ")

  # results of choice
  if choice == "1":
    print("\nYour teammate misses the shot. Your coach and the fans think that you lack confidence and that your a no-good player. You start to receive no playing time \n\nYour career slows down drastically. Your adventure ends here")
  elif choice == "2":
    print(f"\nYou score! Everyone in the stadium is going crazy, chanting your name, {name}!, {name}!, {name}! You have become an amazing player with a really good status. \n\nAlthough you are a great player, you cannot win a championship due to the lack of chemistry and skill that your teammates have. \nYou must choose whether you practice and work hard with your teammate to help improve the team or request a trade.")
    print()

    # use delay to allow user to read text
    time.sleep(4)

    # break off into another choice selection
    print("[1] Work hard to improve team\n[2] Request a trade")
    choice = input("Enter Choice: ")

    # results of choice
    if choice == "1":
      print("\nYou and teammates work hard and improve your team drastically. The chemistry and skill is like no other team. You and your team ends up destroying the playoffs, with no teams able to stop your team\n\n You finally win your championship. Congrats! You have made it to the top of NBA")
    elif choice == "2":
      print("\nYou are able to request a trade, but now everyone sees you as a selfish player. No teams want to sign a contract with you anymore.\n\n You are now without a team and you lost your chance in the NBA. Your adventure ends here.")
