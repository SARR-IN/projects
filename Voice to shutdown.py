# projects

import SpeechRecognition as sr

# Create class
class Gfg:
	
	# Method to take voice commands as input
	def takeCommands(self):
		
		# Using Recognizer and Microphone Method for input voice commands
		r = sr.Recognizer()
		with sr.Microphone() as source:
			print('Listening')
			
			# Number pf seconds of non-speaking audio before
			# a phrase is considered complete
			r.pause_threshold = 0.7
			audio = r.listen(source)
			
			# Voice input is identified
			try:
				
				# Listening voice commands in indian english
				print("Recognizing")
				Query = r.recognize_google(audio, language='en-in')
				
				# Displaying the voice command
				print("the query is printed='", Query, "'")
				
			except Exception as e:
				
				# Displaying exception
				print(e)
				print("Say that again sir")
				return "None"
		return Query
