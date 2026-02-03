import asyncio
import edge_tts

voices = {
    "tamil.wav": ("நான் தமிழ் பேசுகிறேன்", "ta-IN-ValluvarNeural"),
    "malayalam.wav": ("ഞാൻ മലയാളം സംസാരിക്കുന്നു", "ml-IN-SobhanaNeural"),
    "telugu.wav": ("నేను తెలుగు మాట్లాడుతున్నాను", "te-IN-MohanNeural"),
    "kannada.wav": ("ನಾನು ಕನ್ನಡ ಮಾತನಾಡುತ್ತೇನೆ", "kn-IN-GaganNeural"),
    "hindi.wav": ("मैं हिंदी बोलता हूँ", "hi-IN-MadhurNeural"),
    "marathi.wav": ("मी मराठी बोलतो", "mr-IN-AarohiNeural"),
    "english.wav": ("W W W .the s c m silk dot com", "en-IN-NeerjaNeural"),
}

async def main():
    for filename, (text, voice) in voices.items():
        print(f"🔊 Generating {filename} ...")
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(filename)

    print("\n✅ All audio files generated successfully!")

asyncio.run(main())
