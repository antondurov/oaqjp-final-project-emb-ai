'''
Emotion Detector server
'''
from flask import Flask, render_template, request
from EmotionDetection import emotion_detection

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector():
    '''
    Function to analyze the text given
    '''
    text_to_analyze = request.args.get("textToAnalyze")

    result = emotion_detection.emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']
    dominant_emotion = result['dominant_emotion']

    return (f"For the given statement, the system response is 'anger': {anger}, "
    f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
    f"The dominant emotion is {dominant_emotion}")

@app.route("/")
def index():
    '''
    Remders index.html
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
