'''
Emotion Detection
'''
import json
import requests

def emotion_detector(text_to_analyse):
    '''
    emotion detector API service
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/'
    url = url + 'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header, timeout=3)
    
    result = {}
    if response.status_code == 200:
        formatted_res = json.loads(response.text)
        result = formatted_res['emotionPredictions'][0]['emotionMentions'][0]['emotion']
        result['dominant_emotion'] = max(result, key=result.get)
    elif response.status_code == 400:
        result = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    return result
