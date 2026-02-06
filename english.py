import asyncio
import edge_tts
import os

# Default voice controls
DEFAULT_RATE = "-5%"       # speed
DEFAULT_PITCH = "+3Hz"     # tone
DEFAULT_VOLUME = "+0%"

# Output configuration
OUTPUT_DIR = "english_output"
OUTPUT_FILE = "v1.wav"

os.makedirs(OUTPUT_DIR, exist_ok=True)

voices = {
    # "english.wav": (
    #     "Welcome to A V 7 SCM SILK Supplier Portal. "
    #     "This video explains how to book an appointment. "
    #     "Open Google Chrome. "
    #     "In the address bar, type www dot S , C ,M silk dot com and press Enter. "
    #     "The Home Page will open. "
    #     "Click on Login Supplier Portal. "
    #     "Enter your User ID and Password, then click Login. "
    #     "After logging in, all options will appear on the left side. "
    #     "Click on the Appointment option. "
    #     "The Appointment screen will open. "
    #     "The Supplier Name will be auto-displayed. "
    #     "Enter the visitor name. "
    #     "Select the designation. "
    #     ","
    #     " (MD Sir,"
    #     " GM Sir, "
    #     " Manager,"
    #     " Employee,"
    #     " or Others), "
    #     "Enter the visitor mobile number. "
    #     "Enter number of visitors. "
    #     "Select visit date and visit time. "
    #     "Enter purpose of visit. "
    #     "Click Submit. "
    #     "A success alert will be displayed. "
    #     "Click OK. "
    #     "Our management team will contact you. "
    #     "Thank you. Have a good day!",
    #     "en-IN-NeerjaNeural",
    #     "+1%",
    #     "+3Hz"
    # )
    "english.wav": (
    "Hello Sir, "
    "Welcome to the SCM SILK Supplier Portal. "
    "In this video, we will see how to book an appointment step by step. "
    "First, open Google Chrome. "
    "In the search box, type www.the s c m silk.com. "
    "After that, the Home Page will open. "
    "Once the Home Page is opened, click on the Login Supplier Portal option. "
    "Next, it will ask for User ID and Password. "
    "Enter your details correctly and click on Login. "
    "After logging in, "
    "all the options will be shown on the left side. "
    "From there, click on the Appointment option. "
    "Then, the Appointment Screen will open. "
    "There, the Supplier Name will already be auto-displayed. "
    "In the Visitor Name field, "
    "enter the name of the person who is going to visit our office, Sir. "
    "In the Designation field, "
    "select whom the visitor wants to meet, such as "
    "MD Sir, GM Sir, Manager, Employee, or Others, "
    "from the available list. "
    "In the Visitor Mobile Number field, "
    "enter the mobile number of the visitor. "
    "In the No. of Persons Visit field, "
    "mention how many persons are coming to visit. "
    "In the Visit Date field, "
    "select the date on which they are coming to visit. "
    "In the Visit Time field, "
    "mention whether they are coming in the morning or afternoon. "
    "In the Comment Section, "
    "type the purpose of visiting our company. "
    "After filling all the details, "
    "click on the Submit option. "
    "Once you click on Submit, "
    "a Success alert will be shown. "
    "After clicking OK, "
    "our Management Team will contact you, Sir. "
    "Thank you, Sir. "
    "Have a good day!",
    "en-IN-NeerjaNeural",
     "+1%",
     "+1Hz"
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
