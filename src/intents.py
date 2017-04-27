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

    success = make_request('tv/command/poweroff')
    answer = "switching off televison" if success else 'could not switch television off'
    return build_alexa_response(answer, card_title)

def television_hdmi_source(slots):
    card_title = 'Change Hdmi Source'
    print card_title
    sys.stdout.flush()

    success = make_request('tv/command/hdmi')
    answer = "changing hdmi source" if success else 'could not change hdmi source'
    return build_alexa_response(answer, card_title)

def television_tv_source(slots):
    card_title = 'Change TV Source'
    print card_title
    sys.stdout.flush()

    success = make_request('tv/command/tv')
    answer = "changing tv source" if success else 'could not change tv source'
    return build_alexa_response(answer, card_title)

def television_volup(slots):
    card_title = 'Volume Up'
    print card_title
    sys.stdout.flush()

    success = make_request('tv/command/volup')
    answer = "volume up" if success else 'could not increase volume'
    return build_alexa_response(answer, card_title)

def television_voldown(slots):
    card_title = 'Volume Down'
    print card_title
    sys.stdout.flush()

    success = make_request('tv/command/voldown')
    answer = "volume down" if success else 'could not decrease volume'
    return build_alexa_response(answer, card_title)

def television_volup_repeat(slots):
    times = slots['Times']['value']
    card_title = 'Volume Up Repeat'
    print card_title
    sys.stdout.flush()

    success = make_request('tv/command/volup/' + times)
    answer = "volume up" if success else 'could not increase volume'
    return build_alexa_response(answer, card_title)

def television_voldown_repeat(slots):
    times = slots['Times']['value']
    card_title = 'Volume Down Repeat'
    print card_title
    sys.stdout.flush()

    success = make_request('tv/command/voldown/' + times)
    answer = "volume down" if success else 'could not decrease volume'
    return build_alexa_response(answer, card_title)

INTENTS = {
    'TelevisionOff': televison_off,
    'TelevisionChangeHdmiSource': television_hdmi_source,
    'TelevisionChangeTvSource': television_tv_source,
    'TelevisionVolumeUp': television_volup,
    'TelevisionVolumeDown': television_voldown,
    'TelevisionVolumeUpRepeat': television_volup_repeat,
    'TelevisionVolumeDownRepeat': television_voldown_repeat
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
