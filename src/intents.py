import sys
sys.path.insert(0, './lib')

import os
import requests
from requests.auth import HTTPBasicAuth
from src.helper import build_alexa_response, prepare_help_message

def make_request(path):
    host = os.environ.get("HOST_ADDRESS")
    port = os.environ.get("HOST_PORT")
    api_username = os.environ.get("API_USERNAME")
    api_password = os.environ.get("API_PASSWORD")
    url = "http://{}:{}/{}".format(host, port, path)

    print("making request to url {}".format(url))
    response = requests.post(url, timeout=5, auth=HTTPBasicAuth(api_username, api_password))
    if (response.status_code == 200):
        print('request successful!')
        return True
    else:
        print("url {} post failed with status code {}".format(url, response.status_code))
        return False

def televison_off(slots):
    card_title = 'Television Off'
    print card_title
    sys.stdout.flush()

    success = make_request('tv/command/off')
    answer = "switching off televison" if success else 'could not switch television off'
    return build_alexa_response(answer, card_title)

INTENTS = {
    'TelevisionOff': televison_off
}

def on_intent(intent_request, session):
    print("on_intent: requestId={}, sessionId={}".format(intent_request['requestId'], session['sessionId']))

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']
    intent_slots = intent_request['intent'].get('slots',{})

    print("Requested intent: {}".format(intent_name))
    sys.stdout.flush()

    if intent_name in INTENTS:
        return INTENTS[intent_name](intent_slots)
    else:
        build_alexa_response("Sorry, I could not find complete your request.")
