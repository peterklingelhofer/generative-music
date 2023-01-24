import unittest
import librosa
from PIL import Image

class TestAudioToImageConversion(unittest.TestCase):

    def test_conversion(self):
        y, sr = librosa.load("music.wav")

        melFrequencyCepstralCoefficients = librosa.feature.mfcc(y=y, sr=sr)

        melFrequencyCepstralCoefficients = librosa.util.normalize(melFrequencyCepstralCoefficients)

        image = Image.fromarray(melFrequencyCepstralCoefficients, 'RGB')

        self.assertIsNotNone(image)

        self.assertEqual(image.size[0], melFrequencyCepstralCoefficients.shape[1])
        self.assertEqual(image.size[1], melFrequencyCepstralCoefficients.shape[0])

        image.save("audioToImage.png")

if __name__ == '__main__':
    unittest.main()
