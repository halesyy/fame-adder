# Made by JACK HALES under MIT License.
# Add me on LinkedIn: https://www.linkedin.com/in/jack-h-041b32101/
# Or my website:      https://jackhales.com
# Or Facebook:        https://facebook.com/jek.hales

import pyautogui as pag
import sys, json, requests, keyboard, time

reqNames = requests.get("https://snaphame.herokuapp.com/names")
names = reqNames.json()
alreadyUsed = ['one']

print("Got first names: {0}".format(names))
print("Waiting for you to press 'enter' (for fame!)")

while True:
    if keyboard.read_key() == "enter":
        print("Starting mover")
        break

def addName(name):
    # recording where the mouse first started at
    startedAt = pag.position()
    pag.typewrite(name, interval=0.10)
    time.sleep(1)
    moveDown(70)
    # moves down 6 times, down 30 pixels (adjust for bigger/smaller movements)
    for i in range(6):
        pag.click()
        moveDown(22)
    pag.moveTo(startedAt[0], startedAt[1], 1)

    doRefresh()
    pag.moveTo(startedAt[0], startedAt[1], 1)
    moveLeft(50, 0.1)
    pag.click()
    moveRight(50, 0)

# a few functions I wrote to make it easier to move around, since
# pyautogui new versions don't support the move function alone
def moveDown(px, time=0.5):
    now = pag.position()
    pag.moveTo(now[0], now[1]+px, time)

def moveUp(px, time=0.5):
    now = pag.position()
    pag.moveTo(now[0], now[1]-px, time)

def moveRight(px, time=0.5):
    now = pag.position()
    pag.moveTo(now[0]+px, now[1], time)

def moveLeft(px, time=0.5):
    now = pag.position()
    pag.moveTo(now[0]-px, now[1], time)

# a short-cut to refreshing from the start position on certain
# screen size
def doRefresh():
    moveUp(45, 0.2)
    moveLeft(250, 0.2)
    pag.click()
    moveRight(250, 0.2)
    pag.click()


def getNewNames():
    reqNames = requests.get("https://snaphame.herokuapp.com/names")
    # names = reqNames.json()
    return reqNames.json()

for i in range(3):
    time.sleep(5)
    for name in names["names"]:
        if name in alreadyUsed: continue
        addName(name)
        alreadyUsed.append(name)
    names = getNewNames()
