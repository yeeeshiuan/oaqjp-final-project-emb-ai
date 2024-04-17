''' The application of emotion detection 
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app : TODO
app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_analyzer():
    '''
    sent analyzer
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if not response['dominant_emotion']:
        content = 'Invalid text! Please try again!'
    else:
        content = "For the given statement, the system response is "
        content = content + f"'anger': , {response['anger']}"
        content = content + f"'disgust': {response['disgust']}, "
        content = content + f"'fear': {response['fear']}, "
        content = content + f"'joy': {response['joy']}, "
        content = content + f"and 'sadness': {response['sadness']}. "
        content = content + f"The dominant emotion is {response['dominant_emotion']}. "
    return content

@app.route("/")
def render_index_page():
    '''
    render index page
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
