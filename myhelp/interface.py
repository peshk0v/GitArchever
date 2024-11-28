import os
from time import sleep
from art import tprint
from tabulate import tabulate

def system(command):
    os.system(command)

def echo(text):
    os.system(f"echo {text}")

def color(numOfColor):
    os.system(f"color {numOfColor}")

def update():
    os.system(f"clear")

def cmdLines(TrueFalse):
    update()
    if TrueFalse:
        echo("ON")
    else:
        echo("OFF")

def otchot(mode, a, b, delay):
    if mode == 1:
        for i in range(a, b+1):
            print(i)
            sleep(delay)
    elif mode == 2:
        for i in range(a, b+1):
            update()
            print(i)
            sleep(delay)
    elif mode == 3:
        for i in reversed(range(a, b+1)):
            print(i)
            sleep(delay)
    elif mode == 4:
        for i in reversed(range(a, b+1)):
            update()
            print(i)
            sleep(delay)

def loading(text, timeS, fontColor):
    slp = timeS/100
    if fontColor:
        color(fontColor)
    for i in range(100):
        update()
        if i & 1:
            print(f"{text} .")
        elif i & 2:
            print(f"{text} ..")
        else:
            print(f"{text} ...")
        sleep(slp)

def aprint(text):
    tprint(text)

def asleep(time):
    sleep(time)

def textAnimation(text, sleeep):
    ttla = ""
    for i in range(len(text)):
        update()
        ttla += text[i]
        color(i)
        aprint(ttla)
        asleep(sleeep)

def atabulate(list):
    return tabulate(list)