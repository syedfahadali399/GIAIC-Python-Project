import time

def liftoff():
    for i in range(10, 0, -1):
        time.sleep(1)
        print(i)
    print("Lift off!")

liftoff()