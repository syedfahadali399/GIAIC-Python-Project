import time

for i in range(11, 0, -1):
    time.sleep(0.25)
    print(i-1)
    if(i<=1):
      print("Liftoff!")