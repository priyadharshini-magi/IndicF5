import asyncio
import edge_tts
import os

# Default voice controls
DEFAULT_RATE = "-5%"       # speed
DEFAULT_PITCH = "+3Hz"     # tone
DEFAULT_VOLUME = "+0%"

# Output configuration
OUTPUT_DIR = "english_output"
OUTPUT_FILE = "scm2.wav"

os.makedirs(OUTPUT_DIR, exist_ok=True)

voices = {
    "english.wav": (
        "Welcome to SCM SILK Supplier Portal. "
        "This video explains how to book an appointment. "
        "Open Google Chrome. "
        "In the address bar, type www dot SCM silk dot com and press Enter. "
        "The Home Page will open. "
        "Click on Login Supplier Portal. "
        "Enter your User ID and Password, then click Login. "
        "After logging in, all options will appear on the left side. "
        "Click on the Appointment option. "
        "The Appointment screen will open. "
        "The Supplier Name will be auto-displayed. "
        "Enter the visitor name. "
        "Select the designation. "
        "Enter the visitor mobile number. "
        "Enter number of visitors. "
        "Select visit date and visit time. "
        "Enter purpose of visit. "
        "Click Submit. "
        "A success alert will be displayed. "
        "Click OK. "
        "Our management team will contact you. "
        "Thank you. Have a good day!",
        "en-IN-NeerjaNeural",
        "-5%",
        "+3Hz"
    )
}

async def generate(filename, text, voice, rate, pitch):
    rate = rate or DEFAULT_RATE
    pitch = pitch or DEFAULT_PITCH

    output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)

    print(f"🔊 Generating {output_path} | rate={rate}, pitch={pitch}")

    communicate = edge_tts.Communicate(
        text=text,
        voice=voice,
        rate=rate,
        pitch=pitch,
        volume=DEFAULT_VOLUME
    )

    await communicate.save(output_path)

async def main():
    await asyncio.gather(
        *[generate(filename, *data) for filename, data in voices.items()]
    )

    print("\n All audio files saved inside english_output folder!")

#  THIS MUST BE AT FILE ROOT LEVEL
if __name__ == "__main__":
    asyncio.run(main())
