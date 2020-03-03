# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionSendText(Action):

    def name(self) -> Text:
        return "action_send_text"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="This is a sample text from actions")

        return []

class ActionSendImage(Action):

    def name(self) -> Text:
        return "action_send_image"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_image_url("https://i.imgur.com/nGF1K8f.jpg")

        return []

class ActionSendCarousel(Action):

    def name(self) -> Text:
        return "action_send_carousel"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        elements = [{"title": "Sample Title 1",
                    "subtitle": "Sample Subtitle 1",
                     "image_url": "https://i.imgur.com/nGF1K8f.jpg" 
                     },
                    {
                        "title": "Sample Title 2",
                        "subtitle": "Sample Title 2",
                        "image_url": "https://i.imgur.com/nGF1K8f.jpg"
                    },
                    {
                       "title": "Sample Title 3",
                       "subtitle": "Sample Title 3",
                       "image_url": "https://i.imgur.com/nGF1K8f.jpg"
                    }
                    ]
        dispatcher.utter_custom_json(elements)
        return []

class ActionSendButtons(Action):

    def name(self) -> Text:
        return "action_send_buttons"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        text = "Sample Button Replies"
        buttons = [{'title': 'Test Sample Text', 'payload': 'Sample Text', 'content_type': 'text'},
                   {'title': 'Test Sample Image', 'payload': 'Sample Image', 'content_type': 'text'},
                   {'title': 'Test Sample Carousel', 'payload': 'Sample Carousel', 'content_type': 'text'}]
        dispatcher.utter_button_message(text, buttons)
        return []

