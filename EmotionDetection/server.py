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
