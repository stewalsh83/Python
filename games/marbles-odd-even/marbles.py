import random, time, sys


def rules():
    f = open("game-rules.txt", "r")
    print(f.read())


def logo():
    f = open("logo.txt", "r")
    print(f.read())


def win():
    f = open("win.txt", "r")
    return f.read()


def lose():
    f = open("lose.txt", "r")
    return f.read()


def main():
    white = "\33[37m"
    green = "\33[32m"
    red = "\33[31m"
    yellow = "\33[33m"
    blue = "\33[36m"

    game = ["odd", "even"]
    count_marbles_p1 = 5
    computer = 5
    computer_wager = [1, 2, 3]
    game_round = 1
    inner = 0

    print("\n{} {:^50} {}".format(yellow, "Marbles - Odd - Even", white))

    while True:
        try:
            print(yellow, "*" * 50, green)
            logo()
            print('{} {:^50}'.format(blue, "- - - GAME RULES - - -"))
            rules()

            enter = input("\n\tPress enter to start game ")
        except ValueError:
            print(red, "\n Invalid Input!")
        else:
            while count_marbles_p1 > 0 and computer > 0:
                print(yellow, "\nRound:", game_round, white)

                print("Remaining Marbles", count_marbles_p1)
                # wager fix ValueError for invalid input
                wager = int(input("Wager, Between 1 and Remaining Marbles "))

                p1 = input("\nGuess: Does the computer have odd or even? ")
                p2 = random.choice(game)

                if p1 == "odd" and p2 == game[0]:
                    print("You picked odd\nComputer has", p2)
                    count_marbles_p1 += wager
                    computer -= wager
                    print(green, "(Win) My Marbles", count_marbles_p1, "\n Computer Marbles", computer, white)
                    inner = 0

                elif p1 == "odd" and p2 == game[1]:
                    print("You picked odd\nComputer has", p2)
                    count_marbles_p1 -= wager
                    computer += wager
                    print(red, "(Lose) My Marbles", count_marbles_p1, "\n Computer Marbles", computer, white)
                    inner = 1

                elif p1 == "even" and p2 == game[0]:
                    print("You picked even\nComputer has", p2)
                    count_marbles_p1 -= wager
                    computer += wager
                    print(red, "(Lose) My Marbles", count_marbles_p1, "\n Computer Marbles", computer, white)
                    inner = 1

                elif p1 == "even" and p2 == game[1]:
                    print("You picked even\nComputer has", p2)
                    count_marbles_p1 += wager
                    computer -= wager
                    print(green, "(Win) My Marbles", count_marbles_p1, "\n Computer Marbles", computer, white)
                    inner = 0
                else:
                    print(red, "Invalid Input!", white)

                if inner == 1:
                    while inner == 1 and count_marbles_p1 > 0 and computer > 0:
                        print(yellow, "-" * 25, white)
                        game_round += 1
                        print(yellow, "\nRound:", game_round, white)
                        print("Computer Thinking...")
                        time.sleep(5)
                        p2_wager = random.choice(computer_wager)
                        print("Computer Wager", p2_wager)
                        p1 = input("\nLosing Loop - odd or even: ")

                        p2 = random.choice(game)
                        time.sleep(2)

                        if p1 == "odd" and p2 == game[0]:
                            print("-- Computer picked", p2, "\n You have odd")
                            computer -= p2_wager
                            count_marbles_p1 += p2_wager
                            print(green, "-- (Win) My Marbles", count_marbles_p1, "\n Computer Marbles", computer,
                                  white)
                            inner = 0

                        elif p1 == "odd" and p2 == game[1]:
                            print("-- Computer picked", p2, "\n You have odd")
                            computer += p2_wager
                            count_marbles_p1 -= p2_wager
                            print(red, "-- (Lose) My Marbles", count_marbles_p1, "\n Computer Marbles", computer, white)
                            inner = 1
                            print("Losing Loop...")

                        elif p1 == "even" and p2 == game[0]:
                            print("-- Computer picked", p2, "\n You have even")
                            computer += p2_wager
                            count_marbles_p1 -= p2_wager
                            print(red, "-- (Lose) My Marbles", count_marbles_p1, "\n Computer Marbles", computer, white)
                            inner = 1
                            print("Losing Loop...")

                        elif p1 == "even" and p2 == game[1]:
                            print("-- Computer picked", p2, "\n You have even")
                            computer -= p2_wager
                            count_marbles_p1 += p2_wager
                            print(green, "-- (Win) My Marbles", count_marbles_p1, "\n Computer Marbles", computer,
                                  white)
                            inner = 0
                            print("Losing Loop...")
                        else:
                            print(red, "Invalid...", white)

                game_round += 1
                print(yellow, "-" * 25, white)

            if count_marbles_p1 >= 10:
                print(green, win())
                print('{} {:_^50} {}'.format(green, "Congratulations", white))
                break
            if computer >= 10:
                print(red, lose())
                print('{} {:_^50} {}'.format(red, "Try Again", white))
                break


if __name__ == "__main__":
    main()
