from datetime import datetime as dt
import os, glob, random

greetIntent = ["hi", "hello", "hey", "hi there", "hello there", "hey there"]
dateIntent = ["date", "date please", "please tell me date", "what's the date"]
timeIntent = ["time", "time please", "please tell me time", "what's the time"]
musicIntent = ["play song", "please play a song", "play music"]

chat = True
while chat:
    msg = input("Enter your message : ")
    msg = msg.lower()

    if msg in greetIntent:
        print("Hello User")
    elif msg in dateIntent:
        current_date = dt.now().date()
        current_date = current_date.strftime("%d %b, %Y, %a")
        print("Date is :", current_date)
    elif msg in timeIntent:
        current_time = dt.now().time()
        current_time = current_time.strftime("%H:%M:%S, %p")
        print("Time is :", current_time)

    elif msg in musicIntent:
        path = r"D:\Batches\Songs\new_songs"
        os.chdir(path)
        songs = glob.glob("*.mp3")
        os.startfile(random.choice(songs))

    elif msg == "bye":
        print("Bye...")
        break
    else:
        print("I don't understand")
