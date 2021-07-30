import End_Game
from class_Event import Event
from Event_To_Variable_Name_Conversion import Event_To_Variable_Name_Conversion
from Events import *

def Main_Menu_Questioner(Question, Possible_Answers):
	print (Question+ "\n")
	Answer = raw_input().upper()
	return Answer

def Write_Save(nth_event_player_choice_event):
	save_file = open("save.txt", "a")
	#The code below will write the nth event, player choice, and the name of the event itself on 3 separate line
	for index in nth_event_player_choice_event :
		save_file.write(index + "\n")
	save_file.close()

def Read_Save():
	save_file = open("save.txt", "r")
	list_of_nth_event_player_choice_event = [["0", "A", ""]]
	i = 0
	#The code below will take a line that contains the player choice and the corresponding event on the line below it and convert it into a list of event and player choice used throughout the program
	nth_event_player_choice_event = []
	for lines in save_file.readlines():
		i += 1
		#Erasing new line string in the event and player choice and then appending it to a [player choice, event] list
		nth_event_player_choice_event.append(lines.replace("\n",""))
		#Once 2 line have been read i.e. a player choice and its corresponding event, the [player choice, event] will be appended to list of event and player choice, the [player choice, event] list will be wiped clean for the next player choice and event, and the integer i will be reset back to zero
		if i == 3 :
			list_of_nth_event_player_choice_event.append(nth_event_player_choice_event)
			nth_event_player_choice_event = []
			i = 0
		else :
			pass
	save_file.close()
	return list_of_nth_event_player_choice_event
	
def Story_Generator (nth_event_player_choice_event):
	#Because the nth_event could vary in some cases where there are interjected events, it's better to use the event.Name instead of nth_event as a classifier
	#player_choice_and_event is a tuple with the format (player choice, event) e.g. ("A", "Bored At Home")
	player_choice_and_event = (nth_event_player_choice_event[1], nth_event_player_choice_event[2])
	#Convert the given player choice and event to a string of a part of the pre-determined story
	piece_of_story = End_Game.End_Game_Conversion.get(player_choice_and_event)
	#Adding a space after each sentence.
	piece_of_story = piece_of_story + " "
	return piece_of_story

def End_Game_Generator_Printer (list_of_nth_event_player_choice_event):
	#Initialize the story variable as an empty string
	the_story = ""
	#The loop below will take every choices the player made for the experienced event, send it to a separate story generator to get the story, and then append the piece of the story to the overall story
	for nth_event_player_choice_event in list_of_nth_event_player_choice_event :
		the_story = the_story + Story_Generator(nth_event_player_choice_event)
	print "\n"+the_story
	print "\nThanks for playing!"

def Director (list_of_nth_event_player_choice_event):
	#Event mentioned throughout is the event happening in the game
	#Get the most recent nth event, the player's choice in that event and the name of the event itself
	nth_event_player_choice_event = list_of_nth_event_player_choice_event[len(list_of_nth_event_player_choice_event)-1]
	#Convert the event.name from the list to the name of the object (instance of Event class) that can be called
	Name_Of_Event_Variable = Event_To_Variable_Name_Conversion.get(nth_event_player_choice_event[2], "End_Game")
	#The loop below will check every possible continuation of the event that recently happened
	#Event instance that is the last event of a playthrough (also known as End Game Event) will have an empty list as the Answer_For_Next_Event attribute so the loop below will be skipped
	for Answer_For_Next_Event in Name_Of_Event_Variable.Answers_For_Next_Events:
		if nth_event_player_choice_event[1] == Answer_For_Next_Event[0]:
			#Once a match is found with the player's choice, the next event that should happen afterwards for the given answer will be triggered
			Name_Of_Next_Event_Variable = Event_To_Variable_Name_Conversion.get(Answer_For_Next_Event[1])
			#The Questioner_Answer_Checker will be given the most recent nth event plus one because that's the nth event of the next one
			return Name_Of_Next_Event_Variable.Questioner_Answer_Checker(int(nth_event_player_choice_event[0])+1)
		else :
			pass
	#End Game Event will automatically trigger the code below that will generate an ending
	End_Game_Generator_Printer(list_of_nth_event_player_choice_event)
	return "End"
