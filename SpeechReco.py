import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say your password :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
        if text == "admin" :
            print("You are logged in :)")
        else:
            print("Password incorrect")
    except:
        print("Sorry could not recognize what you said")