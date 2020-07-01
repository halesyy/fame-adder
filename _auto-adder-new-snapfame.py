# Made by JACK HALES under MIT License.
# Add me on LinkedIn: https://www.linkedin.com/in/jack-h-041b32101/
# Or my website:      https://jackhales.com
# Or Facebook:        https://facebook.com/jek.hales

import pyautogui as pag
import sys, json, requests, keyboard, time




def getNewNames():
    reqNames = requests.get("https://snaphame.herokuapp.com/names")
    return reqNames.json()

# names = []
reqNames = requests.get("https://snaphame.herokuapp.com/names")
names = reqNames.json()["names"]

print("Retrieved names from Snapfa.me - have you added your name yet?\n".format(names))

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

print("Cords captured: {0}\n".format(anchors))


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



time.sleep(3)
while True:
    for name in names:
        print("Adding {0}".format(name))
        adder(name)
    print("Refreshing names")
    names = getNewNames()["names"]
