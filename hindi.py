import asyncio
import edge_tts
import os

# Default voice controls
DEFAULT_RATE = "-5%"       # speed
DEFAULT_PITCH = "+3Hz"     # tone
DEFAULT_VOLUME = "+0%"

# Output folder name
OUTPUT_DIR = "hindi_output"
OUTPUT_FILE = "scm2.wav"

# Ensure folder exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

voices = {

    "hindi.wav": (
    "A V SEVEN S C M SILK सप्लायर पोर्टल में आपका स्वागत है। "
    "इस वीडियो में SCM SILK सप्लायर पोर्टल में अपॉइंटमेंट कैसे बुक करें, यह स्टेप बाय स्टेप बताया गया है। "
    "सबसे पहले Google Chrome खोलें। "
    "एड्रेस बार में www dot the scm silk dot com टाइप करें और Enter दबाएँ। "
    "होम पेज खुल जाएगा। "
    "Login Supplier Portal पर क्लिक करें। "
    "अपना User name और Password दर्ज करें, फिर Login पर क्लिक करें। "
    "लॉगिन करने के बाद, सभी विकल्प बाईं ओर दिखाई देंगे। "
    "Appointment विकल्प पर क्लिक करें। "
    "Appointment Screen खुल जाएगी। "
    "Supplier Name अपने आप प्रदर्शित होगा। "
    "Visitor Name फ़ील्ड में कार्यालय आने वाले व्यक्ति का नाम दर्ज करें। "
    "Designation फ़ील्ड में यह चुनें कि विज़िटर किससे मिलना चाहता है। "
    "उदाहरण के लिए MD Sir, GM Sir, Manager, Employee, या Others। "
    "विज़िटर का Mobile Number दर्ज करें। "
    "Number of Persons Visit में कुल विज़िटर्स की संख्या दर्ज करें। "
    "Visit Date चुनें। "
    "Visit Time चुनें, Morning या Afternoon। "
    "Comment Section में विज़िट का उद्देश्य लिखें। "
    "सभी विवरण भरने के बाद, Submit पर क्लिक करें। "
    "एक Success Alert दिखाई देगा। "
    "OK पर क्लिक करें। "
    "हमारी Management Team आपसे संपर्क करेगी। "
    "धन्यवाद। आपका दिन शुभ हो।.",
    "hi-IN-SwaraNeural",
    "0%",
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

    print("\n All audio files saved inside hindi_output folder!")

#  THIS MUST BE AT FILE ROOT LEVEL
if __name__ == "__main__":
    asyncio.run(main())
