chat = True

while chat:
    msg = input("Enter your message : ")
    msg = msg.lower()

    if msg == "hi" or msg == "hello" or msg == "hey":
        print("Hello User")
    elif msg == "bye":
        print("Bye...")
        break
    else:
        print("I don't understand")
