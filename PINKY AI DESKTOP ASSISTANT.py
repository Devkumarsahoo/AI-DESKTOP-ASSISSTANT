import pyttsx3 #pip install pyttsx3
import os
import wikipedia
import speech_recognition as sr #pip install speechRecognition
import datetime
import webbrowser
import datetime
import pyaudio #pip install PyAudio
import smtplib #pip install secure-smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)  #INTIALIZING A FEMALE(ZIRA) VOICE



def speak(audio):
	engine.say(audio)
	engine.runAndWait()
	
def wishme():  # CODE TO GREET THE USER

	h=int(datetime.datetime.now().hour)
	print(h)
	if h>0 and h<12:
		speak("good morning dev sahoo!!!")
	elif h>=12 and h<20:
		speak("good evening  dev sahoo!!!")	
			
	else:
		speak("good night  dev sahoo!!!")		
	
def sendmail(to,content):  #CODE SEND TO SEND EMAIL TO RECIEVER

	import smtplib
	smtp=smtplib.SMTP('smtp.gmail.com',587)

	smtp.ehlo()

	smtp.starttls() # for transport layer security

	smtp.ehlo()

	smtp.login("devsahoo@gmail.com","PASSWORD1234")

	smtp.sendmail("devsahoo@gmail.com",to,content)



def takecommand():  #CODE TO TAKE COMMAND(VOICE) OF USER AS INPUT

	r=sr.Recognizer()
	with sr.Microphone() as source:
		print(" Pinky is listening...")
		audio = r.adjust_for_ambient_noise(source)
		#r.pause.threshold=2
		audio=r.listen(source)

	try:
		print("recognizing...")
		query=r.recognize_google(audio,language='en-in')
		print(f"user said :{query}\n")
	
	except LookupError:
		#print(e)
		print("say something..")
		return None
	return query	



speak("Pinky  is intializing...")
speak("      ")
speak("hello dev  sahoo!!!")


if __name__ == '__main__':
	wishme()
	while True:

		query=takecommand().lower()

		if 'wikipedia' in query:             #SEARCHING CONTENT FROM  WIKIPEDIA
			speak("Searching  wikipedia")
			results=wikipedia.summary(query,sentences=2)
			speak(results)
			print(results)

		elif 'open youtube' in query: #OPENING YOUTUBE
			speak("opening youtube  .")
			webbrowser.open("youtube.com")

		elif 'email to dev' in query:	#SENDING A EMAIL
   			
   			try:
   				speak("what should i write")
   				content = takecommand()
   				to= "devsahoo@gmail.com"
   				sendmail(to,content)
   				speak("email has been sent")
   			except LookupError:
	   			speak("email failed !!!!")

		elif 'open google' in query: #OPENING GOOGLE
			speak("google is opening")
			webbrowser.open("google.com")

		elif 'open stackoverflow' in query: #OPENING STACKOVERFLOW
			speak("Stack overflow is opening ")
			webbrowser.open("stackoverflow.com")

		elif 'open wikipedia' in query: #OPENING WIKIPEDIA.COM
			webbrowser.open("wikipedia.com")	
		
		elif 'open notepad' in query: #OPENING NOTEPADE++
   			codePath="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Notepad++"
   			os.startfile(codePath)
