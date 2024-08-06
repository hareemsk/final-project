import requests
import json

def emotion_detector(text_to_analyze):
    # URL for the Emotion Detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Data to be sent to the API
    payload = json.dumps({"text": text_to_analyze})
    
    # Headers for the request
    headers = {'Content-Type': 'application/json'}
    
    # Sending the request to the API
    response = requests.post(url, headers=headers, data=payload)
    
    # Checking if the request was successful
    if response.status_code == 200:
        # Extracting the 'text' attribute from the response
        response_data = response.json()
        return response_data.get('text', 'No text attribute found in response')
    else:
        return f"Error: {response.status_code} - {response.text}"

# Example usage
text_to_analyze = "I'm so happy and excited about this new opportunity!"
result = emotion_detector(text_to_analyze)
print(result)
import requests
import json

def emotion_detector(text_to_analyze):
    # URL for the Emotion Detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Make the API request (this is assumed to be a POST request with the appropriate headers and body)
    response = requests.post(url, json={"text": text_to_analyze})
    
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
    
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
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

# Example usage
result = emotion_detector("I am so happy I am doing this.")
print(result)


