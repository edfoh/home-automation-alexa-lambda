import sys
sys.path.insert(0, './lib')

import os

def build_speechlet_response(title, output, reprompt_text, should_end_session):
  response = {}

  if output:
    response['outputSpeech'] = {
      'type': 'PlainText',
      'text': output
    }
    if title:
      response['card'] = {
        'type': 'Simple',
        'title': title,
        'content': output
      }

  if reprompt_text:
    response['reprompt'] = {
      'outputSpeech': {
        'type': 'PlainText',
        'text': reprompt_text
      }
    }
  response['shouldEndSession'] = should_end_session

  return response

def build_alexa_response(speech = " ", card_title = None, **kwargs):
    session_attrs = {}
    reprompt_text = " "
    end_session = True

    if 'session_attrs' in kwargs:
        session_attrs = kwargs['session_attrs']
    if 'reprompt_text' in kwargs:
        reprompt_text = kwargs['reprompt_text']
    if 'end_session' in kwargs:
        end_session = kwargs['end_session']

    return build_response(session_attrs, build_speechlet_response(card_title, speech, reprompt_text, end_session))

def build_response(session_attributes, speechlet_response):
    response = {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }

    print response
    return response

def prepare_help_message():
    help = "You can ask me to switch off the televison, change channels, change input source and change volume."
    card_title = "Help"
    return build_alexa_response(help, card_title)


def verify_application_id(candidate):
    appId = os.environ.get("SKILL_APPID")
    if appId != None:
        try:
          print "Verifying application ID..."
          if candidate != appId:
            raise ValueError("Application ID verification failed")
        except ValueError as e:
          print e.args[0]
          raise
