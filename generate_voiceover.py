"""Generate voiceover audio files using gTTS."""
from gtts import gTTS
import os
import subprocess
import sys

# Voiceover scripts for each scene
SCENES = {
    "01_title": "We're going to prove one of the most important inequalities in mathematics: the Cauchy-Schwarz inequality. This inequality tells us that the absolute value of the dot product of two vectors is always less than or equal to the product of their lengths.",
    "02_fundamental": "We start with this basic fact: the squared norm of any vector is always non-negative. Here, x and y are vectors, and t is any real number. The expression x minus t times y represents a family of vectors, and its squared norm is always greater than or equal to zero.",
    "03_setup": "Let's expand this expression using the dot product. The squared norm of a vector is equal to the dot product of the vector with itself.",
    "04_expansion1": "First, we distribute the dot product. We get four terms: x dot x, minus t times x dot y, minus t times y dot x, plus t squared times y dot y.",
    "05_expansion2": "Since the dot product is symmetric, x dot y equals y dot x. So we can combine the middle terms to get: norm of x squared, minus 2t times x dot y, plus t squared times norm of y squared.",
    "06_quadratic": "Now we have a quadratic function in t. Let's call it f of t. This is a parabola that opens upward, and it's always above the t-axis because it's always non-negative.",
    "07_discriminant": "For a quadratic function to be always non-negative, its discriminant must be less than or equal to zero. The discriminant is b squared minus 4ac. Let's calculate it.",
    "08_final": "And there we have it! After simplifying, we get: x dot y squared is less than or equal to norm of x squared times norm of y squared. Taking the square root of both sides gives us the Cauchy-Schwarz inequality: the absolute value of x dot y is less than or equal to the product of the norms.",
}

def generate_voiceover():
    """Generate individual voiceover audio files for each scene."""
    os.makedirs("audio", exist_ok=True)
    
    print("Generating voiceover audio files...")
    for scene_name, script in SCENES.items():
        output_file = f"audio/{scene_name}.mp3"
        print(f"  Generating: {output_file}")
        tts = gTTS(text=script, lang='en', slow=False)
        tts.save(output_file)
        print(f"    Done!")
    
    print("\nAll voiceover files generated successfully!")
    print("Files are in the audio/ directory.")

if __name__ == "__main__":
    generate_voiceover()