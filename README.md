# WhatsApp-Online-Tracker
This is a very simple Whatsapp online tracker

Libaries used 
1. Seleinium, with. chrome
2. datetime
3. time
4. playsound

Set Up
1. The user will have 10sec to scan the QR code, the time can be changed in the code
2. In the variable "username" enter the name of the person you want to track, make sure the name is the same as you will find it your chats
3. To see if the person is online or not, the data will be outputed at the console. The online check will take place every 1sec, this value can also be changed from inside of the code
3. You might have to change the path of the chromium and also the beep.mp3 (see before you run it)
4. For mac user, if you are getting an error with the playing of sound, install "PyObjC"

General Information
1. For the program to gather information the chrome window should be open, if the window closes the program will crash. In addition to that your phone should also be connected to the internet, for the whatsapp web to work
2. The sound will only play once for a online session
3. The time is the total time the user was online without going offine

Limitation
1. Can only track one user at a time
2. Need to keep the IDE and chrome window open for it work
3. Has only been tested on MacOS and chrome
4. The user has to be in the first 4 slots of recent chats (best if you can pin the user on top)
5.  
