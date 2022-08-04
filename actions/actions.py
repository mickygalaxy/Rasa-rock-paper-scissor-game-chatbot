# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
import string
from typing import Any, Text, Dict, List
from rasa_sdk import Action,Tracker
from rasa_sdk.executor import CollectingDispatcher
import random

class ActionPlayRPS(Action):
    def name(self)-> Text: 
        return "action_play_rps"
    
    def computer_choice(self) :
        generatednum = random.randint(1,3)
        if generatednum == 1:
            computerchoice = "rock"
            return computerchoice
        elif generatednum == 2:
            computerchoice = "paper"
            return computerchoice
        elif generatednum == 3:
            computerchoice = "scissor" 
            return computerchoice       
    
    def run(self,dispatcher: CollectingDispatcher,tracker: Tracker,domain:Dict[Text,Any])-> List[Dict[Text,Any]]:
        user_choice = tracker.get_slot("choice")
        dispatcher.utter_message(text =f"You chose {user_choice}")
        comp_choice = self.computer_choice()
        dispatcher.utter_message(text=f"The computer chose {comp_choice}")
        
        if user_choice == "rock" and comp_choice == "scissor":
            dispatcher.utter_message(text="Congrats,you won! :-)")
        elif user_choice == "rock" and comp_choice == "paper":
            dispatcher.utter_message(text="The computer won this round :-)")
        elif user_choice == "paper" and comp_choice == "rock":
            dispatcher.utter_message(text="Congrats,you won!")
        elif user_choice == "paper" and comp_choice == "scissor":
            dispatcher.utter_message(text="The computer won this round.")
        elif user_choice == "scissor" and comp_choice == "rock":
            dispatcher.utter_message(text="The computer won this round.")  
        elif user_choice == "scissor" and comp_choice == "paper":
            dispatcher.utter_message(text= "Congrats,you won!")   
        else:
            dispatcher.utter_message(text="It was a title")
            
        return []                        
                 