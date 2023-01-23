from PIL import Image
from pydub import AudioSegment
from pydub.generators import Sine
from tqdm import tqdm

tempo = int(input("Enter the desired tempo (in beat per minute): "))
duration = int(input("Enter the desired duration (in seconds): ")) * 1000

image = Image.open("image.png")
pixels = image.load()

audio = AudioSegment.silent(duration=duration)

pbar = tqdm(total=image.width*image.height)

for x in range(image.width):
    for y in range(image.height):
        color = pixels[x, y]

        frequency = color[0] + color[1] + color[2]

        sine_wave = Sine(frequency).to_audio_segment(duration=50)

        audio = audio + sine_wave

        pbar.update(1)

pbar.close()

audio = audio.speed_change(tempo / audio.frame_rate)

audio.export("music.wav", format="wav")
