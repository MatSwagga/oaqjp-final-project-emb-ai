from EmotionDetection.emotion_detection import emotion_detector as ed
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detection(self):
        result1 = ed("I am glad this happened")
        self.assertEqual(result1['dominant_emotion'],'joy')
        result2 = ed("I am really mad about this")
        self.assertEqual(result2['dominant_emotion'],'anger')
        result3 = ed("I feel disgusted just hearing about this")
        self.assertEqual(result3['dominant_emotion'],'disgust')
        result4 = ed("I am so sad about this")
        self.assertEqual(result4['dominant_emotion'],'sadness')
        result5 = ed("I am really afraid that this will happen")
        self.assertEqual(result5['dominant_emotion'],'fear')

unittest.main()        
