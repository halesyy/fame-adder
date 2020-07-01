# Made by JACK HALES under MIT License.
# Add me on LinkedIn: https://www.linkedin.com/in/jack-h-041b32101/
# Or my website:      https://jackhales.com
# Or Facebook:        https://facebook.com/jek.hales

import pyautogui as pag
import sys, json, requests, keyboard, time, random

try:
    namesFile = open("names.txt", "r")
except:
    print("Could not open names.txt - please make sure this file exists")
    print("...")
    print("Check > https://www.youtube.com/channel/UCsGnqDzdRCAwNEcaT-0kt7g (up-to-date tutorials)")
    input("...")
    exit()

namesData = namesFile.read()
names = namesData.strip().split("\n")

print("Retrieved names from names.txt\n")

anchorNames = ["Add Friend", "Close", "Add Friend Search Bar", "Clear Friend Bar", "First Add Button"]
anchors = []

anchorsFulfilled = 0
anchorsRequired  = len(anchorNames)

print(":: Click enter when your mouse is over '{0}' ::".format(anchorNames[anchorsFulfilled]))

while anchorsFulfilled != anchorsRequired:
    if keyboard.read_key() == "enter":
        mousePositionNow = pag.position()
        anchors.append(mousePositionNow)
        print("Successfully captured mouse coordinates.\n")
        anchorsFulfilled += 1
        if anchorsFulfilled == anchorsRequired: break
        print(":: Click enter when your mouse is over '{0}' ::".format(anchorNames[anchorsFulfilled]))
        time.sleep(1)

print("Cords captured: {0}".format(anchors))

def dragDown(px, time=0.5):
    now = pag.position()
    pag.dragTo(now[0], now[1]+px, time, button='left')

def adder(name):
    global anchors
    addFriend, close, searchBar, clearText, firstAdd  = anchors

    # move to search bar
    pag.moveTo(searchBar[0], searchBar[1], 0.5)
    pag.click()
    time.sleep(1)

    # write out name
    pag.typewrite(name, interval=0.10)
    time.sleep(2)

    # move to first add, then add
    pag.moveTo(firstAdd[0], firstAdd[1], 0.5)
    pag.click()
    time.sleep(2)
    pag.click()
    time.sleep(2)

    #
    # Dragging down, to remove
    dragDown(500)

    # move back to the add area
    pag.moveTo(addFriend[0], addFriend[1], 0.5)
    pag.click()



print("About to infinitely run the adder - will cycle through your name list randomly\n\n")
time.sleep(3)

while True:
    name = random.choice(names)
    print("Adding {0}".format(name))
    adder(name)
    time.sleep(1)
