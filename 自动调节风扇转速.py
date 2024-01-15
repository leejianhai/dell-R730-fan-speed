import os
import time
import select
import sys

def my():
    while True:
        tem = os.popen('sensors')
        context = tem.read()
        for txt in context.splitlines():
            if 'Package id 1:  +' in txt:
                temperature1 = txt.split()[3]
                print(temperature1)
            elif 'Package id 0:  +' in txt:
                temperature2 = txt.split()[3]
                print(temperature2)
            elif "loc1:" in txt:
                temperature3 = txt.split()[1]
                print(temperature3)

        temperature1 = temperature1[1:3]
        temperature2 = temperature2[1:3]
        temperature3 = temperature3[1:3]

        if float(temperature1) > float("60") \
                or float(temperature2) > float("60") \
                or float(temperature3) > float("60"):
            print("温度高")
            os.system("ipmitool -I lanplus -H 192.168.124.35 -U root -P calvin raw 0x30 0x30 0x02 0xff 0x28")
        
        else:
            print("ok")
            os.system("ipmitool -I lanplus -H 192.168.124.35 -U root -P calvin raw 0x30 0x30 0x02 0xff 0xc")

        time.sleep(5)
        print("Enter 'q' to stop: ")
        i, o, e = select.select([sys.stdin], [], [], 5)
        if (i):
            user_input = sys.stdin.readline().strip()
            if user_input == 'q':
                break
        else:
            print("No input. Continuing...")

if __name__ == '__main__':
    my()
