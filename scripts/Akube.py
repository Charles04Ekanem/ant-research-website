#Akube, this is a Mock Pitch Modifier

import librosa

def modify_pitch(input_path, output_path, n_steps=2):
    y, sr = librosa.load(input_path)
    y_shifted = librosa.effects.pitch_shift(y, sr, n_steps=n_steps)
    sf.write(output_path, y_shifted, sr)

# modify_pitch('input.wav', 'accented.wav')