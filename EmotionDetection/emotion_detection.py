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
    formatted_res = json.loads(response.text)
    result = formatted_res['emotionPredictions'][0]['emotionMentions'][0]['emotion']
    result['dominant_emotion'] = max(result, key=result.get)
    return result
