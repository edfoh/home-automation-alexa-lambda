import sys
sys.path.insert(0, './lib')

from src.helper import prepare_help_message, verify_application_id, build_alexa_response
from src.intents import on_intent

def on_session_started(session_started_request, session):
    print("on_session_started: requestId={}, sessionId={}".format(session_started_request['requestId'], session['sessionId']))

def execute(event, context):
    appid = event['session']['application']['applicationId']
    print("lambda_handler: applicationId={}".format(appid))

    #verify_application_id(appid)

    if event['request']['type'] == "LaunchRequest":
        return prepare_help_message()
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    else:
        return build_alexa_response("I received an unexpected request type.")
