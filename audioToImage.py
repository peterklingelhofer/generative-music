import librosa
from PIL import Image

y, sr = librosa.load("music.wav")

melFrequencyCepstralCoefficients = librosa.feature.mfcc(y=y, sr=sr)

melFrequencyCepstralCoefficientsNormalized = librosa.util.normalize(melFrequencyCepstralCoefficients)

grayScaleImage = Image.fromarray(melFrequencyCepstralCoefficientsNormalized, 'L')

grayScaleImage.save("music.png")
