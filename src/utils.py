class ENGLISH_LANG:
    ISO_639_1 = 'en_core_web_md'
    ISO_639 = 'eng'
    ENGLISH_NAME = 'English'

data = {
    "greet": [
        "hello",
        "hey there",
        "howdy",
        "hello",
        "hi",
        "hey",
        "hey ho"
    ],
    "place_info": [
        "i would like to know more about a place",
        "i would like to know more about a city",
        "i would like to know more about the city",
        "i would like to know more about the city of",
        "i would like to know attractions of a place",
        "i would like to know attractions of a city",
        "i would like to know attractions of the city",
        "i would like to know attractions of the city of",
        "what are the main attractions",
        "what are the main attractions of",
        "what are the main attractions of the city",
        "what can I visit in",
        "what can I visit in the city of",
    ],
    "ask_name": [
        "my name is, what is yours?",
        "my name is, what is your name?",
        "what is your name?"
        "whats your name?",
        "what can I call you?"
    ],
    "ask_well_being": [
        "Not so great and you?",
        "i am feeling good and you?",
        "i am feeling good, how about you?",
        "i am feeling great and you?",
        "i am feeling great, how about you?",
        "i am feeling fine and you?",
        "i am feeling fine, how about you?",
        "i am feeling bad and you?",
        "i am feeling weird, how about you?",
        "fine and you?",
        "bad and you?",
        "great and you?",
        "weird and you?",
        "well and you?",
        "not so good and you?",
        "good and you?",
        "bad how about you?",
        "well how about you?",
        "fine how about you?",
        "great how about you?",
        "weird how about you?",
        "good how about you?",
        "not so good how about you?",
        "How about you?",
        "How are you doing?",
        "How are you?",
        "How are you feeling?",
        "How are you feeling today?",
    ],
    "farewell": [
        "goodbye",
        "bye", "see ya later",
        "see you later",
        "bye bye",
        "farewell",
        "gotta go"
    ],
    "deny": [
        "not now",
        "i can't",
        "i cannot",
        "i have to go",
        "no",
        "nah",
        "no thanks"
        "no I can't rate now",
    ],
    "affirm": [
        "sure",
        "of course",
        "ok",
        "yes",
        "yeah",
    ],
    "search_flights": [
        "search",
        "search flights",
        "display flights",
        "i would like to search for flights",
        "i want to travel",
        "search for flights",
        "i am looking for flights",
        "show me flights",
        "show flights",
        "what are the available flights",
        "what are the available flights from to",
        "what flights are available",
        "what flights are available from to",
        "search from to",
        "search flights from to",
        "display flights from to",
        "i would like to search for flights from to",
        "i want to travel from to",
        "search for flights from to",
        "i am looking for flights from to",
        "show me flights from to",
        "show flights from to",
    ],
    "safety_menu": [
        "safety",
        "i would like to know more about safety",
        "safety procedures",
        "show me safety",
        "show me safety procedures",
        "security",
    ],
    "hold_luggage": [
        "bag",
        "luggage",
        "hold luggage",
        "what can i bring in my hold luggage",
        "what can i bring in my bag",
        "what can i bring in my luggage",
        "what items can i have in my hold luggage",
        "what can i carry in my hold luggage",
        "what can i carry in my bag",
        "what can i carry in my luggage",
        "what items can i have in my luggage",
    ],
    "hand_luggage": [
        "hand luggage",
        "what can i bring on my hand luggage",
        "what items can i have in my hand luggage",
    ],
    "smoker": [
        "smoker",
        "can i smoke",
        "can i carry cigarretes and lighter",
        "can i carry a lighter",
        "smoke",
    ],
    "prohibited_items": [
        "prohibited items",
        "show me all the prohibited items",
        "what are the prohibited items",
        "show me prohibited items",
        "show me list of prohibited items",
        "show me list",
        "list",
        "show list",
    ],
    "procedure": [
        "procedure",
        "what should i do if i have any forbidden item",
        "what should i do if i carry a prohibited item",
        "forbidden item",
        "prohibited item",
    ]
}

response_map = {
    "greet": "utter_greet",
    "default": "utter_default",
    "ask_well_being": "utter_ask_well_being",
    "ask_name": "utter_ask_name",
    "ask_name_2": "utter_ask_name_2",
    "user_positive": "utter_user_positive",
    "user_negative": "utter_user_negative",
    "display_menu": "utter_display_menu",
    "farewell": "utter_ask_rate",
    "give_rate": "utter_give_rate",
    "give_opinion": "utter_give_opinion",
    "general_opinion": "utter_general_opinion",
    "experience_positive": "utter_experience_positive",
    "experience_negative": "utter_experience_negative",
    "goodbye": "utter_goodbye",
    "search_flights": "utter_search_flights",
    "city_arrival": "utter_city_arrival",
    "flight_day": "utter_search_flights_day",
    "safety_menu": "utter_safety_menu",
    "hold_luggage": "utter_hold_luggage",
    "hand_luggage": "utter_hand_luggage",
    "smoker": "utter_smoker",
    "prohibited_items": "utter_prohibited_items",
    "procedure": "utter_procedure",
    "place_info": "utter_place_info"
}
