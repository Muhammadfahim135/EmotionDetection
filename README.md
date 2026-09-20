# Final Project

## Emotion Detector

Emotion Detector is a web application built with Flask and Python that analyzes emotional sentiment in text statements using the Watson NLP EmotionPredict service.

## Description
The application evaluates text input and extracts emotional scores across five categories:
- Anger
- Disgust
- Fear
- Joy
- Sadness

It also determines the dominant emotion with the highest score and provides robust error handling for invalid or blank entries.

## Project Structure
- `EmotionDetection/`: Core package containing the `emotion_detector` function.
- `server.py`: Flask web server providing the user interface and API endpoint.
- `templates/`: HTML templates for the web interface.
- `static/`: Static assets (JavaScript client).
- `test_emotion_detection.py`: Unit test suite.

## Getting Started
1. Install dependencies:
   ```bash
   pip install flask requests
   ```
2. Run the application:
   ```bash
   python server.py
   ```
3. Open `http://127.0.0.1:5000` in your web browser.
