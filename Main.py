import Events
import Tools

program_open = True
start_game = False
#Main Loop and Start of Program
while program_open is True :
	#Main Menu
	Main_Menu_Answer = Tools.Main_Menu_Questioner("\nA) New Game\nB) Continue\nC) Exit", ["A", "B", "C"])
	if Main_Menu_Answer == "A" or Main_Menu_Answer == "B" :
		#If the player chooses new game, the program will write a new save file
		if Main_Menu_Answer == "A":
			#Making a new save file
			save_file = open("save.txt", "w")
			save_file.close()
			#Initialize the list of event and player choice
			list_of_nth_event_player_choice_event = [["0", "A", ""]]
		#If the player chooses continue, it will read the previous save file and generate the list of nth event, player choice, and event from there
		else :
			list_of_nth_event_player_choice_event = Tools.Read_Save()
			#Indicating the game has started and initialize the nth event variable
		nth_event =  int(list_of_nth_event_player_choice_event[len(list_of_nth_event_player_choice_event)-1][0]) #The nth event would be the first index of the last index of the list of nth event_player_choice_event e.g. [[0, "A", ""] ["1", "A", "Bored At Home"]]
		start_game = True
		#Gives the player the option to exit to main menu
		print "Remember, you can type 'exit' at any time to exit the game!"
		while start_game is True :
			nth_event_player_choice_event = Tools.Director(list_of_nth_event_player_choice_event)
			list_of_nth_event_player_choice_event.append(nth_event_player_choice_event)
			#If the player is not quitting and the game isn't ending yet, autosave the game
			if nth_event_player_choice_event != "End" and nth_event_player_choice_event != "Exit":
				Tools.Write_Save(nth_event_player_choice_event)
			#Determining if the game has ended or not and if it does, wipe the save and terminate it
			elif nth_event_player_choice_event == "End":
					save_file = open("save.txt", "w")
					save_file.close()
					#Print new line to separate it from the main menu
					print "\n"
					start_game = False
			#Player wants to exit before the game end
			elif nth_event_player_choice_event == "Exit": 
				start_game = False
				program_open = False
	elif Main_Menu_Answer == "C" :
		print ("See you later!")
		#Break the main loop and closes the program
		program_open = False
	#Failsafe against invalid input
	else :
		print "That option doesn't exist\n"
