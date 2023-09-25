from pyAlice.py_alice import PyAlice
import settings

params = {
  "meta": {
    "locale": "ru-RU",
    "timezone": "UTC",
    "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
    "interfaces": {
      "screen": {},
      "payments": {},
      "account_linking": {}
    }
  },
  "session": {
    "message_id": 5,
    "session_id": "5175cbbd-e484-4858-b253-f4c7b4632385",
    "skill_id": "37ccbb22-0b07-4a93-85c0-8517d17ccda7",
    "user": {
      "user_id": "150725BC0540B5EDE3E831A6DB9EFA4F5A3E9BD8BD7F800301393F537B2D40E6"
    },
    "application": {
      "application_id": "EA141820AAB4284BCD741A1D9037A49D06166D2141AAE685F9360C6DEF2853B7"
    },
    "new": False,
    "user_id": "EA141820AAB4284BCD741A1D9037A49D06166D2141AAE685F9360C6DEF2853B7"
  },
  "request": {
    "command": "fun привет мир fun",
    "original_utterance": "привет мир",
    "nlu": {
      "tokens": [
        "привет",
        "мир"
      ],
      "entities": [],
      "intents": {}
    },
    "markup": {
      "dangerous_context": False
    },
    "type": "SimpleUtterance"
  },
  "state": {
    "session": {
      "idd": "idddddddddddd"
    },
    "user": {},
    "application": {}
  },
  "version": "1.0"
}
def handler(event, context):
#   text = "Hello! I\'ll repeat anything you say to me."
#   if "request" in event and \
#           "original_utterance" in event["request"] \
#           and len(event["request"]["original_utterance"]) > 0:
#       text = event["request"]["original_utterance"]
  # return {
  #     "version": event["version"],
  #     "session": event["session"],
  #     "response": {
  #         "text": str(event),
  #         "end_session": "false"
  #   },
  # }

  return PyAlice(params_alice=params, settings=settings)

handler("event", "con")