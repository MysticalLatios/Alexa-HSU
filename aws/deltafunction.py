import boto3

access_key = "AKIAJUDKCKPXUYFFRKFQ"
access_secret = "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"
region ="us-east-1"
queue_url = "https://sqs.us-east-1.amazonaws.com/724334165493/control_tasks"

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }

def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }

def post_message(client, message_body, url):
    response = client.send_message(QueueUrl = url, MessageBody= message_body)
    
def lambda_handler(event, context):
    client = boto3.client('sqs', aws_access_key_id = access_key, aws_secret_access_key = access_secret, region_name = region)
    intent_name = event['request']['intent']['name']
    if intent_name == "turnOnProjector":
        post_message(client, 'Pon', queue_url)
        message = "On"
    elif intent_name == "turnOffProjector":
        post_message(client, 'Poff', queue_url)
        message = "off"
    elif intent_name == "inputLaptop":
        post_message(client, 'Laptop', queue_url)
        message = "input is now on laptop"
    elif intent_name == "inputDesktop":
        post_message(client, 'Desktop', queue_url)
        message = "input is now on desktop"
    else:
        message = "Unknown"
        
    speechlet = build_speechlet_response("Projector Status", message, "", "true")
    return build_response({}, speechlet)
