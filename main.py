import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import webbrowser
import wikipedia
import pyjokes
import PyPDF2
import rotatescreen

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
    except:
        pass
    return command
print("hello I am Tom! your virtual assistant")
talk("hello I am Tom your virtual assistant")
print("How may I help you?")
talk("How may I help you?")

def run_alexa():
    command = take_command()
    if 'tom' in command:
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing' + song)
            pywhatkit.playonyt(song)
        elif 'hello' in command:
            print('hello charan')
            talk('hello charan whats up')
        elif 'weather' in command:
            print('Just go and look at outside')
            talk('just go and look at outside')
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            talk('the time is' + time)
        elif 'google' in command:
            person = command.replace('google', '')
            print("searching your results...")
            talk('searching about' + person)
            webbrowser.open('https://google.com/?#q=' + person)
        elif 'tell me about' in command:
            person = command.replace('tell me about', '')
            info = wikipedia.summary(person, 2)
            print(info)
            talk(info)
        elif 'date' in command:
            talk('sorry, look at your calender')
        elif 'joke' in command:
            print(pyjokes.get_joke())
            talk(pyjokes.get_joke())
        elif 'message' in command:
            print('message will be sent as per your schedule')
            talk('message will be sent as per your schedule')
            pywhatkit.sendwhatmsg('+91 9876543210', 'Its a scheduled msg:)', 23, 56)
        elif 'read' in command:
            engine = pyttsx3.init()
            book = open('krishna.pdf', 'rb')
            pdfReader = PyPDF2.PdfFileReader(book)
            pages = pdfReader.numPages
            print(pages)
            speaker = pyttsx3.init()
            for num in range(1, pages):
                page = pdfReader.getPage(1)
                text = page.extractText()
                speaker.say(text)
                speaker.runAndWait()
        elif 'rotate'and 'normal' in command:
            screen = rotatescreen.get_primary_display()
            screen.rotate_to(0)
        elif 'rotate' and 'reverse' in command:
            screen = rotatescreen.get_primary_display()
            screen.rotate_to(180)
        elif 'rotate' and 'left' in command:
            screen = rotatescreen.get_primary_display()
            screen.rotate_to(270)
        elif 'rotate' and 'right' in command:
            screen = rotatescreen.get_primary_display()
            screen.rotate_to(90)
        elif 'see you' in command:
            print('bye bye have a nice day charan')
            talk('bye bye have a nice day charan')
            breakpoint()
        else:
            talk('please say the command again.')
    else:
        print('sorry I hurted, I am tom :(')
        talk('sorry I hurted, I am tom')
while 1:
    run_alexa()
