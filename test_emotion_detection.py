import unittest
from unittest.mock import patch, MagicMock
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):

    def _create_mock_response(self, emotions_dict):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "emotionPredictions": [
                {
                    "emotion": emotions_dict
                }
            ]
        }
        return mock_response

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_joy(self, mock_post):
        mock_post.return_value = self._create_mock_response({
            'anger': 0.013622335,
            'disgust': 0.0017160782,
            'fear': 0.008164097,
            'joy': 0.9679419,
            'sadness': 0.04002049
        })
        result = emotion_detector("I am glad this happened")
        for key in ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']:
            self.assertIn(key, result)
        self.assertEqual(result['dominant_emotion'], 'joy')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_anger(self, mock_post):
        mock_post.return_value = self._create_mock_response({
            'anger': 0.892341,
            'disgust': 0.014210,
            'fear': 0.021550,
            'joy': 0.003112,
            'sadness': 0.068787
        })
        result = emotion_detector("I am really mad about this")
        for key in ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']:
            self.assertIn(key, result)
        self.assertEqual(result['dominant_emotion'], 'anger')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_disgust(self, mock_post):
        mock_post.return_value = self._create_mock_response({
            'anger': 0.025514,
            'disgust': 0.852104,
            'fear': 0.015423,
            'joy': 0.004128,
            'sadness': 0.102831
        })
        result = emotion_detector("I feel disgusted just hearing about this")
        for key in ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']:
            self.assertIn(key, result)
        self.assertEqual(result['dominant_emotion'], 'disgust')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_sadness(self, mock_post):
        mock_post.return_value = self._create_mock_response({
            'anger': 0.025514,
            'disgust': 0.003125,
            'fear': 0.015423,
            'joy': 0.004128,
            'sadness': 0.951810
        })
        result = emotion_detector("I am so sad about this")
        for key in ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']:
            self.assertIn(key, result)
        self.assertEqual(result['dominant_emotion'], 'sadness')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_fear(self, mock_post):
        mock_post.return_value = self._create_mock_response({
            'anger': 0.014231,
            'disgust': 0.002890,
            'fear': 0.884512,
            'joy': 0.005421,
            'sadness': 0.092946
        })
        result = emotion_detector("I am really afraid that this will happen")
        for key in ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']:
            self.assertIn(key, result)
        self.assertEqual(result['dominant_emotion'], 'fear')


if __name__ == '__main__':
    unittest.main()
