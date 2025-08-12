from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector as ed

app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def emotion_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    if text_to_analyze:
        response = ed(text_to_analyze)
        anger = str(response["anger"])
        disgust = str(response["disgust"])
        fear = str(response["fear"])
        joy = str(response["joy"])
        sadness = str(response["sadness"])
        dominant_emotion = str(response["dominant_emotion"])
        return f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)
