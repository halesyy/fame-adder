# Made by JACK HALES under MIT License.
# Add me on LinkedIn: https://www.linkedin.com/in/jack-h-041b32101/
# Or my website:      https://jackhales.com
# Or Facebook:        https://facebook.com/jek.hales

import pyautogui as pag
import sys, json, requests, keyboard, time, pyperclip

print("Leave the below field empty if you want us to pick a proven message...\n")
yourMessage = input("What do you want to paste into each chat?: ")

if yourMessage == "":
    print("Set your message as the default..")
    yourMessage = "Hey there, (just added you from Snapfame). If you send my username to your friends, I'll do the same and boost your account on Snapfame (http://snapfa.me) :P"
    # yourMessage = "Sorry for the spam message - I'm Jack, testing out a tool and you're one of the lucky people I added to test it from http://snapfa.me"

print("\nWaiting for you to press 'enter' (for fame!)")
while True:
    if keyboard.read_key() == "enter":
        print("Starting mover")
        break

# Action:
# 0. Ask user if they wish to use a message, or if not just give
#    them a random message?
# 1. Wait for enter, sitting over someone's username
# 2. Click (going to open the profile)
# 3. Paste message (from api, or local random array)
#    Hit enter
# 4. Swipe back (click, drag out - OR - have a point of interest where the user goes back - IF CASE - move back and re-structure starting point)
# 5. Drag down X pix - OR - move down pix amount, that limits though..
# 6. Repeat this process

# Dragging is possible! Use the function `pyautogui.dragTo(100, 200, button='left')` as a guide for this
# Great, this will have to be adapted into a more abstract function to get in and out of areas
# such as the chat.

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

def dragLeft(px, time=0.5):
    now = pag.position()
    pag.dragTo(now[0]-px, now[1], time, button='left')

def dragUp(px, time=0.5):
    now = pag.position()
    pag.dragTo(now[0], now[1]-px, time, button='left')

pyperclip.copy(yourMessage)

timesDoingRightMove = 0

def downRightAmount():
    postBeforeDrag = pag.position()
    dragUp(120, time=0.5)
    pag.moveTo(postBeforeDrag[0], postBeforeDrag[1])

for i in range(10):
    pag.click()
    time.sleep(1.5)
    pag.hotkey('ctrl', 'v')
    time.sleep(0.3)
    pag.press('enter')
    time.sleep(0.3)
    postBeforeDrag = pag.position()
    dragLeft(225, time=0.4)
    pag.moveTo(postBeforeDrag[0], postBeforeDrag[1])
    time.sleep(1)
    time.sleep(2)

    # iterate this up, once it's over 3, stop doing the down right move
    timesDoingRightMove += 1
    if timesDoingRightMove <= 6:
        downRightAmount()


# downRightAmount()
# time.sleep(2)
# downRightAmount()
