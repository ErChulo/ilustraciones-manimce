"""Stitch video clips and add voiceover audio."""
import subprocess
import os
import glob

def get_duration(video_path):
    """Get video duration in seconds using ffprobe."""
    cmd = [
        'ffprobe',
        '-v', 'error',
        '-show_entries', 'format=duration',
        '-of', 'default=noprint_wrappers=1:nokey=1',
        video_path
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return float(result.stdout.strip())

def main():
    # Video clips in order
    video_clips = [
        "media/videos/script/1080p60/CauchySchwarzTitle.mp4",
        "media/videos/script/1080p60/CauchySchwarzFundamental.mp4",
        "media/videos/script/1080p60/CauchySchwarzSetup.mp4",
        "media/videos/script/1080p60/CauchySchwarzExpansion1.mp4",
        "media/videos/script/1080p60/CauchySchwarzExpansion2.mp4",
        "media/videos/script/1080p60/CauchySchwarzQuadratic.mp4",
        "media/videos/script/1080p60/CauchySchwarzDiscriminant.mp4",
        "media/videos/script/1080p60/CauchySchwarzFinal.mp4",
    ]
    
    # Voiceover audio files
    audio_files = [
        "audio/01_title.mp3",
        "audio/02_fundamental.mp3",
        "audio/03_setup.mp3",
        "audio/04_expansion1.mp3",
        "audio/05_expansion2.mp3",
        "audio/06_quadratic.mp3",
        "audio/07_discriminant.mp3",
        "audio/08_final.mp3",
    ]
    
    print("Checking video clips...")
    for clip in video_clips:
        if not os.path.exists(clip):
            print(f"  ERROR: Missing video clip: {clip}")
            return
        duration = get_duration(clip)
        print(f"  {os.path.basename(clip)}: {duration:.2f}s")
    
    print("\nChecking audio files...")
    for audio in audio_files:
        if not os.path.exists(audio):
            print(f"  ERROR: Missing audio file: {audio}")
            return
        print(f"  {os.path.basename(audio)}: exists")
    
    # Create concat file for video
    print("\nCreating video concatenation file...")
    with open("video_list.txt", "w") as f:
        for clip in video_clips:
            f.write(f"file '{clip}'\n")
    
    # Concatenate video clips
    print("Concatenating video clips...")
    subprocess.run([
        'ffmpeg', '-y',
        '-f', 'concat',
        '-safe', '0',
        '-i', 'video_list.txt',
        '-c', 'copy',
        'combined_video.mp4'
    ], check=True)
    
    # Concatenate audio files
    print("Concatenating audio files...")
    with open("audio_list.txt", "w") as f:
        for audio in audio_files:
            f.write(f"file '{audio}'\n")
    
    subprocess.run([
        'ffmpeg', '-y',
        '-f', 'concat',
        '-safe', '0',
        '-i', 'audio_list.txt',
        '-c', 'copy',
        'combined_audio.mp3'
    ], check=True)
    
    # Get video duration
    video_duration = get_duration("combined_video.mp4")
    print(f"\nTotal video duration: {video_duration:.2f}s")
    
    # Add audio to video
    print("Adding voiceover to video...")
    subprocess.run([
        'ffmpeg', '-y',
        '-i', 'combined_video.mp4',
        '-i', 'combined_audio.mp3',
        '-c:v', 'copy',
        '-c:a', 'aac',
        '-shortest',
        'cauchy_schwarz_inequality.mp4'
    ], check=True)
    
    # Cleanup
    print("Cleaning up temporary files...")
    os.remove("video_list.txt")
    os.remove("audio_list.txt")
    os.remove("combined_video.mp4")
    os.remove("combined_audio.mp3")
    
    final_video = "cauchy_schwarz_inequality.mp4"
    if os.path.exists(final_video):
        final_size = os.path.getsize(final_video) / (1024 * 1024)  # MB
        print(f"\n✓ Final video created: {final_video}")
        print(f"  Size: {final_size:.2f} MB")
        print(f"  Duration: {video_duration:.2f}s")
    else:
        print("\n✗ Error creating final video")

if __name__ == "__main__":
    main()