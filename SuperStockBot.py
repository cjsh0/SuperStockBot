import time
import requests
import os
from datetime import datetime
from random import randint
from pushbullet import pushbullet

# Read user settings
with open("settings.conf") as fr:
    chosenSettings = fr.readlines()

# Initialize list to hold parsed settings
rawSettings = []

# Loop through and parse user settings
for j in chosenSettings:
    strippedLine = j.strip()
    currentSplit = strippedLine.split("=")
    rawSettings.append(currentSplit[1])

# Instantiate pushbullet w/ API key
pb = pushbullet.Pushbullet(rawSettings[1])

# Set file path to notification sound
notifSound = "ding.wav"
# Enable notification ding
notifSoundFlag = int(rawSettings[0])

# Read working list of URLs to check
with open(rawSettings[2]) as fileToRead:
    fileContent = fileToRead.readlines()

# Strip any \n chars
fileContent = [x.strip() for x in fileContent]

# Assign read in data to working list
workingList = fileContent

# Initialize variable to store response from requested URL
skuPage = ""

# Begin main loop, performing checks
while True:
    # String to look for when served with a potentially OOS item, dynamic based upon which site we are checking
    if ("bestbuy" in workingList[0]):
        oosMessage = "http://schema.org/soldout"
    else:
        oosMessage = "#######"
    
    # User-agent headers to circumvent insta-block
    headers = {'User-agent': 'Mozilla/5.0'}

    for x in workingList:
        # Random sleep, simple ban-hammer avoidance
        time.sleep(randint(int(rawSettings[3]), int(rawSettings[3]) + 1))
        # Store response converted to lowercase
        skuPage = requests.get(x, headers = headers).text.lower()

        # Check to see if response body contains out of stock flag
        if (oosMessage in skuPage):
            # Print OOS message
            print(datetime.now().strftime("%H:%M:%S") + " [OOS] " + x)
        else:
            # Print to console result
            print(datetime.now().strftime("%H:%M:%S") + " [!IN STOCK!] " + x)
            
            # Build body string for notification
            bodyString = datetime.now().strftime("%H:%M:%S") + ": [IN STOCK] " + x
            
            # Send notification via Pushbullet
            push = pb.push_note("STOCK ALERT", bodyString)

            if (notifSoundFlag != 0):
                os.system("aplay ding.wav")