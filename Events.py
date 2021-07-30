from class_Event import Event

#The event 0 that when ran through the Director will lead to the first event
Start = Event(
	"Start",
	"Start of the game",
	"",
	[],
	#The only important part of this instance is the second index of the first index of the list below, which should be filled with the name of the first event to then be triggered by the director
	[["A", "Bored_At_Home"]]
)

#Events that are going to happen
Bored_At_Home = Event(
	#Name of the event, which is the stringified name of this event instance
	"Bored_At_Home",
	#What the event is about
	"You're bored and hungry at home.",
	#What choices are given to player in the event
	"What do you do?\nA) Go to a restaurant\nB) Go to the cinema\n",
	#Valid answer that the player can give. If the player doesn't answer with the string below the question will only be repeated. Has to be uppercase because Questioner_Answer_Checker convert player's answer into uppercase.
	["A", "B"],
	#List of possible continuation of the story. Consisting of a list with a possible answer as the first index and the name of the event tht should happen if the player answered that possible answer
	[["A", "Restaurant"], ["B", "Cinema"]]
)

Restaurant = Event(
	"Restaurant",
	"You're at a restaurant.",	
	"What do you order?\nA) Pasta\nB) Spaghetti\n",
	["A", "B"],
)

Cinema = Event(
	"Cinema",
	"You're at a cinema.",
	"What movie do you want to see?\nA) Jaws\nB) Star Wars\n",
	["A", "B"],
)
