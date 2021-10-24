import datetime, time, winsound


def alarm():
    alarm = input("   Set Alarm: hh:mm:ss \n\t  --> ")
    print("\n")
    while True:
        x = datetime.datetime.now()
        list_of_times = []

        times = x.strftime("%X")
        list_of_times.append(times)

        t = ''.join(list_of_times)

        if t == alarm:
            print("\n       Alarm: " + t)
            break
        # (optional) comment out else statement
        else:
            # print(t)
            print(f'\r       Clock: {t}', end='', flush=True)
            time.sleep(1)


def sound():
    duration1 = 1000  # milliseconds
    freq1 = 500  # Hz

    duration2 = 250
    freq2 = 400

    winsound.Beep(freq1, duration1)
    winsound.Beep(freq2, duration2)


def main():
    start = datetime.datetime.now()
    print('\n  Start Time: {}\n'.format(start.strftime("%X")))
    alarm()
    sound()


if __name__ == "__main__":
    main()
