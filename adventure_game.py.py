import time
import random


def print_story(intro_message):
    print(intro_message)
    time.sleep(2)


def intro(random_enemy, random_attribute):
    print_story("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_story(f"Rumor has it that a {random_attribute} {random_enemy} "
                "is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_story("In front of you is a house.")
    print_story("To your rigth is a dark cave.")
    print_story("In your hand you hold your trusty "
                "(but not very effective) dagger. \n")


def first_decision():
    print_story("Enter 1 to knock on the door of the house.")
    print_story("Enter 2 to peer into the cave.")
    first = input("What would you like to do? \n(Please enter 1 or 2) \n")


def play_again():
    again = input("\nWould you like to play again? (y/n)")
    if again == "y":
        print_story("Excellent! Restarting the game...")
        play_game()
    elif again == "n":
        print_story("Thanks for playing! See you next time.")
    else:
        print_story("Invalid answer. Please try again")
        play_again()


def fight(have_sword, random_enemy, random_attribute):
    if have_sword is False:
        print_story("You do your best...")
        print_story("but your dagger is no match for "
                    f"the {random_attribute} {random_enemy}.")
        print_story("You have been defeated!")
        play_again()
    else:
        print_story(f"As the {random_attribute} {random_enemy} "
                    "moves to attack, you unsheath your new sword.")
        print_story("The Sword of Ogoroth shines brightly in your "
                    "hand as you brace yourself for the attack.")
        print_story(f"But the {random_attribute} {random_enemy} takes "
                    "one look at your shiny new toy and runs away!")
        print_story("You have rid the town of the "
                    f"{random_attribute} {random_enemy}. YOU ARE VICTORIOUS!")
        play_again()


def house(have_sword, random_enemy, random_attribute):
    print_story("You approach the door of the house.")
    print_story("You are about to knock when the door opens "
                f"and out steps a {random_attribute} {random_enemy}.")
    print_story(f"Eep! This is the {random_enemy}'s house!")
    print_story(f"The {random_enemy} attacks you!")
    if have_sword is False:
        print_story("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.")
    else:
        print_story("You feel extremely prepared since "
                    "now you have a new amazing sword")


def cave(have_sword):
    print_story("You peer cautiously into the cave.")
    if have_sword is False:
        print_story("It turns out to be only a very small cave.")
        print_story("Your eye catches a glint of metal behind a rock.")
        print_story("You have found the magical Sword of Ogoroth!")
        print_story("You discard your silly old dagger "
                    "and take the sword with you.")
    else:
        print_story("You've been here before, and gotten all "
                    "the good stuff. It's just an empty cave now.")
    print_story("You walk back out to the field. \n")


def fight_or_run(have_sword, random_enemy, random_attribute):
    fight_run = input("Would you like to (1) fight or (2) run away? \n")

    if fight_run == "1":
        fight(have_sword, random_enemy, random_attribute)
    elif fight_run == "2":
        print_story("You run back into the field. "
                    "Luckily, you don't seem to have been followed. \n")
        whole_story(have_sword, random_enemy, random_attribute)
    else:
        print_story("You can choose between 1 and 2. Please try again")
        fight_or_run(have_sword, random_enemy, random_attribute)


def whole_story(have_sword, random_enemy, random_attribute):
    print_story("Enter 1 to knock on the door of the house.")
    print_story("Enter 2 to peer into the cave.")
    first_decision = input("What would you like to do?"
                           "\n(Please enter 1 or 2) \n")
    # knock on the door of the house
    if first_decision == "1":
        house(have_sword, random_enemy, random_attribute)
        # fight or run away
        fight_or_run(have_sword, random_enemy, random_attribute)

    # peer into the cave
    elif first_decision == "2":
        cave(have_sword)
        have_sword = True
        whole_story(have_sword, random_enemy, random_attribute)
    else:
        print_story("You can choose between 1 and 2. Please try again")
        whole_story(have_sword, random_enemy, random_attribute)


def play_game():
    have_sword = False
    random_enemy = random.choice(['spider', 'pirate', 'kraken', 'troll'])
    random_attribute = random.choice(['weird', 'pretty', 'stinky', 'gigant'])
    intro(random_enemy, random_attribute)
    whole_story(have_sword, random_enemy, random_attribute)


play_game()
