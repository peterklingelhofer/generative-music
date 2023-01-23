from PIL import Image
from pydub import AudioSegment
from pydub.generators import Sine
from tqdm import tqdm

duration = int(input("Enter the desired duration (in seconds): ")) * 1000

image = Image.open("image.png")
pixels = image.load()

audio = AudioSegment.silent(duration=duration)

pbar = tqdm(total=image.width * image.height)

for x in range(image.width):
    for y in range(image.height):
        color = pixels[x, y]

        frequency = color[0] + color[1] + color[2]

        sineWave = Sine(frequency).to_audio_segment(duration=50)

        audio = audio + sineWave

        pbar.update(1)

pbar.close()

audio.export("music.wav", format="wav")
