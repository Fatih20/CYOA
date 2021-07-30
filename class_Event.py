class Event :
	def __init__(self, Name, Occurence, Question, Possible_Answer, Answers_For_Next_Events = []):
		#Question is a string of the question
		#Possible_Answer a list filled with a string of possible answer e.g. ["A", "B"]
		#Answers for next events is a list consisting of a list with a possible answer in the first index and the name of the next event that happens should player's chooses that answer
		self.Name = Name
		self.Occurence = Occurence
		self.Question = Question
		self.Possible_Answer = Possible_Answer
		self.Answers_For_Next_Events = Answers_For_Next_Events
	
	#Printing the question, taking player's choice, and checking the answer in one function
	def Questioner_Answer_Checker (self, nth_event):
		Question_Done = False
		while Question_Done is False :
			#Print the question but also informs the player how to exit the game
			#Convert the player answer to uppercase because the Possible_Answer attribute is formatted in lowercase
			Answer = raw_input("\n"+self.Occurence + " "+self.Question +"\n\nType 'exit' if you want to exit the game"+ "\n\n").upper()
			#If the player type e because they want to exit the game, this function will return that, triggering the main loop to stop
			if Answer.upper() == "EXIT" :
				return "Exit"
			else :
				for Possible_Answer in self.Possible_Answer:
					if Answer == Possible_Answer:
						return [str(nth_event),Answer, self.Name]					
					else :
						pass
				print "\nThat option doesn't exist\n"
