import unittest
from PIL import Image
from pydub import AudioSegment
from pydub.generators import Sine
from tqdm import tqdm

class TestImageToAudioConversionWithProgressBar(unittest.TestCase):

    def test_conversion(self):

        duration = int(input("Enter the desired duration (in seconds): ")) * 1000

        image = Image.open("image.png")
        pixels = image.load()

        audio = AudioSegment.silent(duration=duration)
        total = image.width * image.height
        pbar = tqdm(total=total)
        print(total)
        durationPerPixel = duration/total
        for x in range(image.width):
            for y in range(image.height):
                color = pixels[x, y]

                frequency = color[0] + color[1] + color[2]

                sineWave = Sine(frequency).to_audio_segment(duration=durationPerPixel) # divide by total?

                audio = audio + sineWave

                pbar.update(1)

        # Check that the audio is not None
        self.assertIsNotNone(audio)

        # Check that the audio has the correct duration
        self.assertEqual(len(audio), duration)

        pbar.close()

        audio.export("music.wav", format="wav")

if __name__ == '__main__':
    unittest.main()