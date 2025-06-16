#Nsin-Uyom (This script adds Noise to Audio)

from pydub import AudioSegment
import random

def inject_noise(clean_path, noise_folder, output_path, snr_db=10):
    clean = AudioSegment.from_file(clean_path)
    noise_files = [f for f in os.listdir(noise_folder) if f.endswith('.wav')]
    noise = AudioSegment.from_file(os.path.join(noise_folder, random.choice(noise_files)))

    if len(noise) < len(clean):
        noise = noise * (len(clean) // len(noise) + 1)
    noise = noise[:len(clean)]

    noise = noise - (noise.dBFS - (clean.dBFS - snr_db))
    noisy_audio = clean.overlay(noise)
    noisy_audio.export(output_path, format='wav')

# inject_noise('clean.wav', 'noise_library/', 'noisy_output.wav')