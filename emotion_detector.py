import requests #import to handle HTTP requests
'''
Method takes 'text_to_analyze' and runs 
it through an emotion dection. 
Then the method returns the result in
json object
'''
def emotion_detector(text_to_analyze):
    #Url to access Watson NLP
    url = (
        'https://sn-watson-emotion.labs.skills.'
        'network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    #Headers to access Watson NLP
    headers = {
        "grpc-metadata-mm-model-id":
         "emotion_aggregated-workflow_lang_en_stock"
    }
    #JSON object
    myobj = {"raw_document":{"text": text_to_analyze}}
    response = requests.post(url,json=myobj,headers=headers)
    return response.text
