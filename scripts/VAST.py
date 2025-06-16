#Voice and Audio Signal Transform (Plots Waveform of input signals)

import matplotlib.pyplot as plt

def visualize_audio(audio_path):
    y, sr = librosa.load(audio_path)
    plt.figure(figsize=(10, 4))
    librosa.display.waveshow(y, sr=sr)
    plt.title('Audio Waveform')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.tight_layout()
    plt.savefig('waveform.png')
    plt.show()

# visualize_audio('speech.wav'), accepts .wav files