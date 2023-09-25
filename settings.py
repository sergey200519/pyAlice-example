from pyAlice.functions import end_alice_event

import buttons, key_words, more_data_messages

EVENTS = True
DEBUG = True
LOG_OUTPUT_IMMEDIATELY = True
TIME_ZONE = None


TEXT_FOR_KEY_WORDS = "command"
VERSION = "1.0"


ALL_MESSAGES = {
    "start_message": "Hello World",
    "error_message": "ERROR",
    "help": "Help",
    "end_message": "конец"
}
STARTING_MESSAGE = "start_message"
ERROR_MESSAGE = "error_message"
HELP_MESSAGE = "help"
MORE_DATA_MESSAGES = more_data_messages.more_data_messages

EVENTS_LIST = {
    "endAliceEvent": end_alice_event,
}
IGNORE_EVENTS_LIST = ["storageFillEvent"]

BUTTONS = buttons.buttons
BUTTONS_GROUPS = {}
STARTING_BUTTONS = []

KEY_WORD = key_words.key_words

DEBUG_LANGUAGE = "ru"
LANGUAGE = "ru"
SOURCE_TEXT = "command"
