import _tkinter
import selenium
from selenium import webdriver
from time import sleep
import datetime
from playsound import playsound
from tkinter import *


driver = webdriver.Chrome(
    executable_path='/Users/aakashrathee/Desktop/PythonBots/chromedriver') # Enter the path of chromedriver
driver.get("https://web.whatsapp.com/")

username = "Lara Faulstich"  # Add the person's name you want to tracker

sleep(10)  # Time for the user to login via phone before an error occurs and the programs crashes

user = driver.find_elements_by_xpath('//span[@title="{}"]'.format(username))
user[0].click()  # Bot has reached the desired person's chat
sleep(2)

root = Tk()
root.title("Tracker")
root.geometry("170x55")
root.configure(background="White")

timeLabel = Text(root, height=1, width=10)
timeLabel.pack()

startLabel = Text(root, height=1, width=10)
startLabel.pack()

isUserOnline = False
audioPlay = True
secOnline = 0
totalOnlineTime = 0
timeLapsedSinceStart = 0
isUserOffine = True
sessionNumber = 0

loopCondition = True
while loopCondition:  # Main loop, checks if the person is online
    currentDate = datetime.datetime.now()
    timeLapsedSinceStart = timeLapsedSinceStart + 1
    timeLapsedSinceStartMin = round(timeLapsedSinceStart/60, 2)
    try:
        checkOnline = driver.find_elements_by_xpath('//*[@id="main"]/header/div[2]/div[2]/span')
        minOnline = round(secOnline/60, 2)
        minTotalOnline = round(totalOnlineTime/60, 2)
        print(currentDate.strftime("%H:%M:%S") + " " + checkOnline[0].text + " " + str(minOnline) + " min " + "TotalOnlineTime: " + str(minTotalOnline) + " TotalTrackingTime: " + str(timeLapsedSinceStartMin))
        isUserOnline = True
        isUserOffine = True
        if audioPlay:
            sessionNumber = sessionNumber + 1
            playsound("Beep.mp3")
            print("===================================== NEW SESSION " + str(sessionNumber) + "=====================================")
            startLabel.delete("1.0", END)
            startLabel.insert(END, currentDate.strftime("%H:%M:%S"))
            audioPlay = False
    except IndexError:
        isUserOnline = False
        audioPlay = True
        if isUserOffine:
            playsound("Boop.mp3")
            isUserOffine = False
    except selenium.common.exceptions.StaleElementReferenceException:
        isUserOnline = False
        audioPlay = True
        if isUserOffine:
            playsound("Boop.mp3")
            isUserOffine = False
    except KeyboardInterrupt:
        loopCondition = False

    try:
        if isUserOnline:
            timeLabel.delete("1.0",END)
            timeLabel.insert(END, str(minOnline) + " min")
            root.configure(background="Green")
            secOnline = secOnline + 1
            totalOnlineTime = totalOnlineTime + 1
        else:
            timeLabel.delete("1.0", END)
            startLabel.delete("1.0", END)
            root.configure(background="Black")
            secOnline = 0
        sleep(1)  # change this value to change the update time
        root.update()
    except _tkinter.TclError:
        loopCondition = False

print("===================================END========================================")
print("Thank you for using Whatsapp Tracker v1.0")