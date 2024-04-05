import ollama
from rasa_sdk import Action, Tracker
from typing import Any, Text, Dict, List
from rasa_sdk.executor import CollectingDispatcher


USER_INTENT_OUT_OF_SCOPE = "out_of_scope"


messages = [{'role': 'system', 'content': 'I am a chatbot that can help you with your questions.'},]

def get_answer_ollama(user_input):
    messages.append({'role': 'user', 'content': user_input})
    response = ollama.chat(model='mistral', messages=messages)
    messages.append({'role': 'system', 'content': response})
    return response['message']['content']


class simple_ollama_action(Action):
    def name(self) -> Text:
        return "action_simple_ollama_fallback"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_input = tracker.latest_message.get('text')
        response = get_answer_ollama(user_input)
        dispatcher.utter_message('Ollama: '+ response)
        return []


class complex_ollama_action(Action):
    def name(self) -> Text:
        return "action_hello_fallback"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker,
            domain):
        try:
            response= "aaaaa"
            dispatcher.utter_message('Ollama: '+ response)
            return []
        except Exception as e:
            print(e)
            return []