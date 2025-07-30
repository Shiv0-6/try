# app.py
from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
import random

app = Flask(__name__)

@app.route('/generate-questions', methods=['POST'])
def generate_questions():
    video_url = request.json.get('url')
    video_id = video_url.split('v=')[1].split('&')[0]  # Extract video ID
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    # Simple question generation from transcript
    questions = []
    for entry in transcript:
        text = entry['text']
        questions.append(f"What did the speaker say about: {text[:30]}...?")  # Create a question

    random_questions = random.sample(questions, min(5, len(questions)))  # Get 5 random questions
    return jsonify(random_questions)

if __name__ == '__main__':
    app.run(debug=True)
