# This is an Audio-Video sync checker, ensures audio and video sync

from moviepy.editor import VideoFileClip
import librosa
import tempfile
import os

def check_sync_in_video(video_path, tolerance=0.2):
    clip = VideoFileClip(video_path)
    video_duration = clip.duration

    # Extract audio to temp file
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
        temp_audio_path = temp_audio.name
        clip.audio.write_audiofile(temp_audio_path, verbose=False, logger=None)

    # This Loads audio and gets duration
    y, sr = librosa.load(temp_audio_path, sr=None)
    audio_duration = len(y) / sr

    os.remove(temp_audio_path)  # Clean up, deletes temporary audio file

    # Sync check
    print(f"Video Duration: {video_duration:.2f}s")
    print(f"Audio Duration: {audio_duration:.2f}s")
    if abs(video_duration - audio_duration) > tolerance:
        print("Audio and video may be out of sync.")
    else:
        print("Synchronised!")

# Example usage
check_sync_in_video("example_video.mp4")
