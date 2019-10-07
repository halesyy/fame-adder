## This Python-based keyboard and mouse controller runs the motions of automatically adding people through a Teamviewer connection to a phone with Snapchat installed. It pulls from the Snaphame API to gather names that wish to be added.

# Fame (Snaphame)

Use the power of community to get seen and help your career. A Snapchat auto-adder. Data comes from https://snaphame.herokuapp.com/ (fill that out before using the application so that as many names can be instilled into the root of the app).

## Pre-requirements

- A windows computer (raw Python works on Mac/Linux)
- A phone which can simulate presses from Teamviewer QuickConnect (Android-tested)
-

## Quick install

1. Get Teamviewer QuickConnect on your phone with Snapchat installed
2. Download Teamviewer on your computer that you wish to operate the code on
3. (With Python): Download and run AutoAdder.py (`python AutoAdder.py`)
4. (Without Python): Download and run AutoAdder.exe (Windows only)

Now that you have everything installed, you should see **Waiting for you to press 'enter' (for fame!)**

![image of terminal waiting for user to press ender for snapchat auto adder](https://i.gyazo.com/30ce3e38741334bd36c89526e637c209.png)

This is going to wait in the background till you press enter to start adding the users in the cache.

From here, you'll want to open your Teamviewer-to-phone connection, open Snapchat, go to the add friends area and make sure that you text box is selected and ready to type letters - NOW, you need to place your cursor over this area:

![image of snapchat connected phone on teamviewer using the snapchat auto adder and where it has to sit, next to the "Find friends" button where there's a small snapcode button](https://i.gyazo.com/9148285136cff24ce8597b0500db4b63.png)

If you don't wish to alter the pixels numbers in the code itself, to find the right position reference the rough size from this 1920x1080 monitor to find where the screen size may best work for you:

![desktop image of how to use a snapchat auto adder to add friends without you even being there](https://i.gyazo.com/08d43f58809c1875917b706c810bb2b6.jpg)

NOTE: change lines 61/63 of AutoAdder.py to change how far the pixels move left/right if there's a discrepency, I can't imagine all phone screens are the same size...



## Behind the reason this is so elaborate

This means Snapchat cannot ban you, because you are NOT using a 3rd party API (strictly against ToS). Instead, you are **simply using a disability-enabled service to assist in the adding of your friends**. Snapchat has no ToS violations against adding people you may not know, so this is a completely safe alternative to auto-adding friends.
