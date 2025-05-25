from creature import Creature

def main():
    print("Welcome to the Companion Creature Game.")
    name = input("Please name your pet: ")

    pet = Creature(name)
    print(f"\n{name} has joined you. Take care of it wisely.")

    day = 1
    actions_today = 0

    print(f"\nDay {day} begins.")
    pet.show_status()

    while pet.alive:
        print("\nChoose an action: bathe / rest / decorate / talk / status / quit")
        command = input(">> ").strip().lower()

        if command == "bathe":
            pet.bathe()
            actions_today += 1
        elif command == "rest":
            pet.rest()
            actions_today += 1
        elif command == "decorate":
            pet.decorate()
            actions_today += 1
        elif command == "talk":
            pet.talk()
            actions_today += 1
        elif command == "status":
            pet.show_status()
            continue  #Status check doesn't count
        elif command == "quit":
            print(f"\nThank you for spending time with {pet.nickname}.")
            break
        else:
            print("Invalid command. Please try again.")
            continue

        #After 3 actions, simulate one full day
        if actions_today >= 3:
            print(f"\nDay {day} has ended. Your pet goes to sleep.")
            pet.decay()
            pet.check_condition()

            day += 1
            actions_today = 0

            if pet.alive:
                print(f"\nDay {day} begins. Status has changed overnight.")
                pet.show_status()

    print("Game over.")

if __name__ == "__main__":
    main()
