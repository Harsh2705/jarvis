import pyttsx3

import datetime

import speech_recognition as sr

from pydub import AudioSegment
from pydub.playback import play

import webbrowser

import wikipedia

engine=pyttsx3.init()

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishme():
	hour=int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
		speak("good morning sir")

	elif hour>=12 and hour<18:
		speak("good afternoon sir")

	else:
		speak("good evening sir")

	speak("hii sir how are you ")

def takecommand():
	r=sr.Recognizer()
	with sr.Microphone() as source:
		print("listening : ")
		audio=r.listen(source)

		try:
			print("recognize ")
			query=r.recognize_google(audio)
			print("user said :: ")

		except:
			print("say again")
			return 'none'
		return query

wishme()

while True:

	query=takecommand().lower()

	if 'play punjabi song' in query:
		song=AudioSegment.from_mp3('gun.mp3')
		play(song)
		song=AudioSegment.from_mp3('dilgit.mp3')
		play(song)
		song=AudioSegment.from_mp3('Pink.mp3')
		play(song)

	elif 'play sapna chaudhary song' in query:
		song=AudioSegment.from_mp3('daman.mp3')
		play(song)
		song=AudioSegment.from_mp3('chetak.mp3')
		play(song)

	elif 'play ammy virk song' in query:
		song=AudioSegment.from_mp3('wang.mp3')
		play(song)

	elif 'play jordan song' in query:
		song=AudioSegment.from_mp3('botal.mp3')
		play(song)
		song=AudioSegment.from_mp3('mashoor.mp3')
		play(song)
		song=AudioSegment.from_mp3('jatiye.mp3')
		play(song)
		song=AudioSegment.from_mp3('future.mp3')
		play(song)

	elif 'play top punjabi song' in query:
		song=AudioSegment.from_mp3('lakk.mp3')
		play(song)
		song=AudioSegment.from_mp3('jhalla.mp3')
		play(song)

		song=AudioSegment.from_mp3('patole.mp3')
		play(song)

	elif 'play haryanvi song' in query:
		song=AudioSegment.from_mp3('gulzaar.mp3')
		play(song)
		song=AudioSegment.from_mp3('gulzaar1.mp3')
		play(song)
		song=AudioSegment.from_mp3('gulzaar2.mp3')
		play(song)
		song=AudioSegment.from_mp3('gulzaar3.mp3')
		play(song)

		
		
		
		



	elif 'hi jarvis' in query:
		speak("hi sir")

	elif 'your name' in query:
		speak("i am jarvis")

	elif 'how are you jarvis' in query:
		speak("i am fine sir and you")

	elif 'i am fine' in query:
		speak("ok ")

	elif 'say hello' in query:
		speak("hello sir")

	elif 'bye bye jarvis' in query:
		speak("bye bye sir have a nice day")

	elif 'thank you jarvis' in query:
		speak("is okay sir")

	elif 'my introduction' in query:
		speak("you are my boss and i am your assitant")
		speak(" your name is harsh rana and your father name is bhupender rana ")
		speak("you belong to anwerpur barouli")
		speak("you are a student and your college name is u p group of college")

	elif 'talk to me' in query:
		speak("hello sir  how are you ")
		speak("what are you make a new code today")

	elif 'the time' in query:
		strTime = datetime.datetime.now().strftime("%H:%M:%S")  
		print(strTime)  
		speak("Sir, the time is ")

	elif 'open file' in query:
		file = open('arogyasetu.py', 'r') 
		print file.read()

	elif 'open youtube' in query:
		webbrowser.open("http://youtube.com/#q=")

	elif 'open google' in query:
		webbrowser.open("http://google.com/#q=")

	elif 'wikipedia' in query:
		speak("searching wikipedia")
		results = wikipedia.summary(query, sentences=2)
		print(results)
		speak(results)




	else:
		speak("sorry sir")