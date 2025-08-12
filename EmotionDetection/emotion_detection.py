import json
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
    #formatted_response is the main dictionary returned by your API call,
    # converted from JSON format into a Python dictionary.
    formatted_response = json.loads(response.text)
    emotions_data = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotions_data['anger']
    disgust_score = emotions_data['disgust']
    fear_score = emotions_data['fear']
    joy_score = emotions_data['joy']
    sadness_score = emotions_data['sadness']    
    dominant_emotion = max(emotions_data, key=emotions_data.get)
    
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }


    