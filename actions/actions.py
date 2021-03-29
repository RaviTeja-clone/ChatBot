# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from datetime import datetime, timedelta


class ActionCleanRoomRelative(Action):

    def name(self) -> Text:
        return "action_clean_room_relative"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        hours = int(tracker.get_slot("no_of_hours"))
        time = datetime.now() + timedelta(hours=hours)
        hour = format(time, "%I")
        am_pm = time.strftime("%p")

        dispatcher.utter_message(text="Sure, I have scheduled a cleaing for {} {} today".format(hour, am_pm))

        return []
