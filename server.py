'''
Server for Emotion Detector app.
Renders template when root is accessed, then once the user 
enters text into the input field, the app analyzes it and provides
an emotional rating for the user’s input.
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector as ed

app = Flask("Emotion Detector")

@app.route('/')
def home():
    """
    Renders index.html template when application is run.
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector():
    """
    Takes textToAnalyze with GET request from
    mywebscript.js then analyzes the text with emotion_detector.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = ed(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    anger = str(response["anger"])
    disgust = str(response["disgust"])
    fear = str(response["fear"])
    joy = str(response["joy"])
    sadness = str(response["sadness"])
    dominant_emotion = response["dominant_emotion"]

    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
