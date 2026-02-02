import asyncio
import edge_tts

async def main():
    text = "நான் தமிழ் பேசுகிறேன்"
    voice = "ta-IN-ValluvarNeural"

    communicate = edge_tts.Communicate(text, voice)
    await communicate.save("output.wav")

    print("✅ Tamil audio saved as output.wav")

asyncio.run(main())
