import asyncio
import edge_tts
import os

# Default voice controls
DEFAULT_RATE = "-5%"       # speed
DEFAULT_PITCH = "+3Hz"     # tone
DEFAULT_VOLUME = "+0%"

# Output folder name
OUTPUT_DIR = "tamil_output"
OUTPUT_FILE = "scm1.wav"

# Ensure folder exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

voices = {
    "tamil.wav": (
        "S C M SILK Supplier Portal க்கு வரவேற்கிறோம். "
        "S C M SILK Supplier Portal க்கு Appointment எவ்வாறு பதிவு செய்வது என்பதை படிப்படியாக பார்க்கலாம். "
        "Google Chrome ஐ திறக்கவும். "
        "Search Box-ல் www.Thee S C M silk dot com என்று type செய்து Enter அழுத்தவும். "
        "Home Page open ஆகும். "
        "Login Supplier Portal click செய்யவும். "
        "உங்கள் User name மற்றும் Password ஐ enter செய்யவும், Login click செய்யவும். "
        "உள்நுழைந்த பிறகு, அனைத்து Option இடது பக்கத்தில் காணப்படும். "
        "Appointment option click செய்யவும். "
        "Appointment Screen open ஆகும். "
        "Supplier Name தானாகவே (Auto Display) காண்பிக்கப்படும். "
        "Visitor Name பகுதியில், எங்கள் அலுவலகத்திற்கு வருகை தரும் நபரின் பெயரை குறிப்பிடவும். "
        "Designation பகுதியில், சந்திக்க விரும்பும் நபரைத் தேர்வு செய்யவும். "
        "MD Sir, GM Sir, Manager, Employee, அல்லது Others. "
        "வருகையாளரின் Mobile Number enter செய்யவும். "
        "Number of Persons Visit பகுதியில் மொத்த வருகையாளர்களின் எண்ணிக்கையை குறிப்பிடவும். "
        "Visit Date பகுதியில், வருகை தரும் தேதியைத் தேர்வு செய்யவும். "
        "Visit Time தேர்வு செய்யவும் Morning அல்லது Afternoon. "
        "Comment Section இல் வருகையின் நோக்கத்தை குறிப்பிடவும். "
        "அனைத்து விவரங்களையும் நிரப்பிய பிறகு, Submit என்ற option click செய்யவும். "
        "Success Alert காண்பிக்கப்படும். "
        "OK என்பதை click செய்யவும். "
        "எங்கள் Management Team உங்களை தொடர்பு கொள்வார்கள். "
        "நன்றி. நல்ல நாளாக அமைய வாழ்த்துக்கள்.",
        "ta-IN-PallaviNeural",
        "-0%",
        "+3Hz"
    ),
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

    print("\n All audio files saved inside tamil_output folder!")

#  THIS MUST BE AT FILE ROOT LEVEL
if __name__ == "__main__":
    asyncio.run(main())
