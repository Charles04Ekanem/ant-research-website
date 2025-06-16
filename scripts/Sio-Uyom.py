#Sio-Uyom, This is an Audio Cleaner (Denoiser)

import noisereduce as nr
import soundfile as sf

def clean_audio(input_path, output_path):
    data, rate = sf.read(input_path)
    reduced_noise = nr.reduce_noise(y=data, sr=rate)
    sf.write(output_path, reduced_noise, rate)

# clean_audio('input.wav', 'cleaned_output.wav')