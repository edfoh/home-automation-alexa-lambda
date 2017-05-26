import sys
sys.path.insert(0, './lib')

import os
import requests
from requests.auth import HTTPBasicAuth
from src.helper import build_alexa_response

def post_request(path):
    host = os.environ.get("HOST_ADDRESS")
    port = os.environ.get("HOST_PORT")
    api_username = os.environ.get("API_USERNAME")
    api_password = os.environ.get("API_PASSWORD")
    url = "http://{}:{}/{}".format(host, port, path)

    print("making POST request to url {}".format(url))
    response = requests.post(url, timeout=30, auth=HTTPBasicAuth(api_username, api_password))
    if response.status_code == 200:
        print('request successful!')
        return True, None
    elif repsonse.status_code == 400:
        return False, response.json()['message']
    else:
        print("url {} post failed with status code {}".format(url, response.status_code))
        return False, None

def get_request(path):
    host = os.environ.get("HOST_ADDRESS")
    port = os.environ.get("HOST_PORT")
    api_username = os.environ.get("API_USERNAME")
    api_password = os.environ.get("API_PASSWORD")
    url = "http://{}:{}/{}".format(host, port, path)

    print("making GET request to url {}".format(url))
    response = requests.get(url, timeout=30, auth=HTTPBasicAuth(api_username, api_password))
    if (response.status_code == 200):
        print('request successful!')
        return response.json()
    else:
        print("url {} get failed with status code {}".format(url, response.status_code))
        return None

def chromecast_test(slots):
    card_title = 'Chromecast Test'
    print card_title
    sys.stdout.flush()

    return build_alexa_response('Working!', card_title)

def chromecast_get_playlist(slots):
    card_title = 'Chromecast Playlist'
    print card_title
    sys.stdout.flush()

    body = get_request('youtube/playlist')
    if body == None:
        return build_alexa_response('could not get playlist', card_title)
    else:
        answer = 'Here is your playlist! {}'.format(','.join(body['playlist']))
        return build_alexa_response(answer, card_title)

def chromecast_stop(slots):
    card_title = 'Chromecast Stop'
    print card_title
    sys.stdout.flush()

    success, err_message = post_request('chromecast/stop')
    answer = 'ok' if success else 'could not stop'
    return build_alexa_response(answer, card_title)

def chromecast_play_first_video_in_playlist(slots):
    playlist_name = slots['PlaylistName']['value']
    card_title = 'Chromecast Play First Video In Playlist'
    print card_title
    sys.stdout.flush()

    success = post_request('chromecast/play/playlist/{}'.format(playlist_name))
    answer = 'Playing playlist {}'.format(playlist_name) if success else 'could not play playlist {}'.format(playlist_name)
    return build_alexa_response(answer, card_title)

def chromecast_pause(slots):
    card_title = 'Chromecast Pause'
    print card_title
    sys.stdout.flush()

    success, err_message = post_request('chromecast/pause')
    answer = 'ok' if success else err_message
    return build_alexa_response(answer, card_title)

def chromecast_play(slots):
    card_title = 'Chromecast Play'
    print card_title
    sys.stdout.flush()

    success, err_message = post_request('chromecast/play')
    answer = 'ok' if success else err_message
    return build_alexa_response(answer, card_title)

def chromecast_resume(slots):
    card_title = 'Chromecast Resume'
    print card_title
    sys.stdout.flush()

    success, err_message = post_request('chromecast/resume')
    answer = 'ok' if success else err_message
    return build_alexa_response(answer, card_title)

def chromecast_play_next(slots):
    card_title = 'Chromecast Play Next'
    print card_title
    sys.stdout.flush()

    success, err_message = post_request('chromecast/play/next')
    answer = 'ok' if success else err_message
    return build_alexa_response(answer, card_title)

def chromecast_play_previous(slots):
    card_title = 'Chromecast Play Previous'
    print card_title
    sys.stdout.flush()

    success, err_message = post_request('chromecast/play/previous')
    answer = 'ok' if success else err_message
    return build_alexa_response(answer, card_title)

INTENTS = {
    'ChromecastTest': chromecast_test,
    'ChromecastGetPlaylist': chromecast_get_playlist,
    'ChromecastPlayFirstVideoInPlaylist': chromecast_play_first_video_in_playlist,
    'ChromecastStop': chromecast_stop,
    'ChromecastPause': chromecast_pause,
    'ChromecastPlay': chromecast_play,
    'ChromecastResume': chromecast_resume,
    'ChromecastPlayNext': chromecast_play_next,
    'ChromecastPlayPrevious': chromecast_play_previous
}

def on_chromecast_intent(intent_request, session):
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
