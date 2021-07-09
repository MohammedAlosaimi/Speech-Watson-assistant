import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# This class to convert the text to speech and then store it in mp3 file
import textospeech

# this import to play the mp3 file
import os

apikey = "xRNztS37oq2zmm77WlCCBhadjVzuEykPOF-R2iUzT16L"
url = "https://api.eu-de.assistant.watson.cloud.ibm.com/instances/933848e9-b27d-4be4-801c-31c65bf6d016"

assistantId = "005f2265-e3b6-49ad-87cf-010d39238265"

# Setup Service
authenticator = IAMAuthenticator(apikey)
# New Assistant Service
assistant = AssistantV2(
    version='2020-04-01',
    authenticator = authenticator
)
# Set Service URL
assistant.set_service_url(url)

def watsonAssistantChat(text):

    # Response msg from the assistant service
    response = assistant.message_stateless(
    assistant_id=assistantId,
    input={
        'message_type': 'text',
        'text': text
    }
    ).get_result()

    # change the response to a json string
    msg = json.dumps(response)

    result = "Sorry, there is a problem with the response"

    # Loads the msg and the return the result.
    data = json.loads(msg)
    if "output" in data:
        result = data['output']['generic'][0]['text']
  
    # Print the assistant reply
    print("* Assistant reply")
    print(result)
    
    # Convert the text to speech and then store it in mp3 file
    textospeech.storeMP3File(result)

    # Playing the output.mp3 file 
    print("* Playing the assistant reply")
    os.system('output.mp3')
    print("* done playing reply")


# print(watsonAssistantChat("hi"))

# print(json.dumps(response, indent=2))