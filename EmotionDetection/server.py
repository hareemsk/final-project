from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_endpoint():
    data = request.get_json()
    text_to_analyze = data.get('text', '')
    
    # Call the emotion_detector function to get the emotion analysis
    emotion_result = emotion_detector(text_to_analyze)
    
    # Format the response as required
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {emotion_result['anger']}, "
        f"'disgust': {emotion_result['disgust']}, "
        f"'fear': {emotion_result['fear']}, "
        f"'joy': {emotion_result['joy']} and "
        f"'sadness': {emotion_result['sadness']}. "
        f"The dominant emotion is {emotion_result['dominant_emotion']}."
    )
    
    return jsonify({'message': formatted_response})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

import requests
import json

def emotion_detector(text_to_analyze):
    # Check for blank input
    if not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # URL for the Emotion Detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Make the API request
    response = requests.post(url, json={"text": text_to_analyze})
    
    # Handle a bad request (status code 400)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # Convert the response text to a dictionary
    response_dict = json.loads(response.text)
    
    # Extract the relevant emotion scores
    emotions = response_dict.get('emotion', {})
    
    anger_score = emotions.get('anger', 0)
    disgust_score = emotions.get('disgust', 0)
    fear_score = emotions.get('fear', 0)
    joy_score = emotions.get('joy', 0)
    sadness_score = emotions.get('sadness', 0)
    
    # Determine the dominant emotion
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    
    dominant_emotion = max(emotion_scores, key=emotion_scores.get) if any(emotion_scores.values()) else None
    
    # Prepare the final output format
    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    
    return result
