import random


def coin_toss():
    h, t, i = 0, 0, 0
    coin = ["Heads", "Tails"]

    white = "\33[37m"
    green = "\33[32m"
    red = "\33[31m"
    yellow = "\33[33m"
    blue = "\33[34m"
    sky_blue = "\33[36m"

    while True:
        try:
            count = int(input("\33[33mEnter number of coin tosses \33[37m"))
        except ValueError:
            print(red, "\nInvalid Input,\nTry Again.\n", white)
        else:
            while i < count:
                toss = random.choice(coin)
                if toss == coin[0]:
                    h += 1
                else:
                    t += 1
                i += 1
            print("Heads = ", h, "Tails = ", t)
            break


coin_toss()
