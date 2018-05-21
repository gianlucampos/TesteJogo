import threading
import time
import keyboard


def thread1():
    if threading.active_count() <= 4:
        while not keyboard.is_pressed('r'):
            print("Rodando Thread 1!")
            time.sleep(0.1)
    else:
        print("muitas threads rodando".upper())
        time.sleep(1)


def main():
    while not keyboard.is_pressed('q'):
        if keyboard.is_pressed('t'):
            thread_1 = threading.Thread(target=thread1, name="thread1")
            thread_1.start()

        time.sleep(1)
        print("Rodando Main")
        print("{} threads rodando - {}".format(threading.active_count(), threading.enumerate()))


if __name__ == '__main__':
    main()
