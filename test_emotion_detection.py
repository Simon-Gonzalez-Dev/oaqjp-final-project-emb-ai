from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detection(self):
        result1 = emotion_detector("I am glad this happened")
        self.assertEqual(result1['dominant_emotion'], 'joy_score')
        result2 = emotion_detector("I am really mad about this")
        self.assertEqual(result2['dominant_emotion'], 'anger_score')
        result3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result3['dominant_emotion'], 'disgust_score')
        result4 = emotion_detector("I am so sad about this")
        self.assertEqual(result4['dominant_emotion'], 'sadness_score')
        result5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result5['dominant_emotion'], 'fear_score')

unittest.main()