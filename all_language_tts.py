import asyncio
import edge_tts

voices = {
    # 🇮🇳 Indian Languages
    "tamil.wav": (
        "வணக்கம். தமிழ் ஒரு பழமையான மற்றும் செழுமையான மொழியாகும். இது உலகம் முழுவதும் பேசப்படுகிறது.",
        "ta-IN-ValluvarNeural"
    ),
    "malayalam.wav": (
        "നമസ്കാരം. മലയാളം ഇന്ത്യയിലെ കേരള സംസ്ഥാനത്തിലെ പ്രധാന ഭാഷയാണ്.",
        "ml-IN-SobhanaNeural"
    ),
    "telugu.wav": (
        "నమస్కారం. తెలుగు భారతదేశంలో ఎక్కువగా మాట్లాడే భాషలలో ఒకటి.",
        "te-IN-MohanNeural"
    ),
    "kannada.wav": (
        "ನಮಸ್ಕಾರ. ಕನ್ನಡ ಕರ್ನಾಟಕ ರಾಜ್ಯದ ಅಧಿಕೃತ ಭಾಷೆ.",
        "kn-IN-GaganNeural"
    ),
    "hindi.wav": (
        "नमस्कार। हिंदी भारत की प्रमुख भाषाओं में से एक है।",
        "hi-IN-MadhurNeural"
    ),
    "marathi.wav": (
        "नमस्कार. मराठी ही महाराष्ट्र राज्याची प्रमुख भाषा आहे.",
        "mr-IN-AarohiNeural"
    ),
    "bengali.wav": (
        "নমস্কার। বাংলা একটি মিষ্টি এবং সমৃদ্ধ ভাষা।",
        "bn-IN-TanishaaNeural"
    ),
    "gujarati.wav": (
        "નમસ્કાર. ગુજરાતી એક સુંદર અને સરળ ભાષા છે.",
        "gu-IN-DhwaniNeural"
    ),
    "punjabi.wav": (
        "ਸਤ ਸ੍ਰੀ ਅਕਾਲ। ਪੰਜਾਬੀ ਇੱਕ ਜੀਵੰਤ ਭਾਸ਼ਾ ਹੈ।",
        "pa-IN-GurleenNeural"
    ),
    "urdu.wav": (
        "السلام علیکم۔ اردو ایک خوبصورت زبان ہے۔",
        "ur-IN-SalmanNeural"
    ),

    # 🌍 International Languages
    "english.wav": (
        "Hello. Welcome to SCM SILK Supplier Portal",
        "en-IN-AartiNeural"
    ),
    "french.wav": (
        "Bonjour. Le français est une langue élégante et largement parlée.",
        "fr-FR-DeniseNeural"
    ),
    "german.wav": (
        "Hallo. Deutsch ist eine wichtige Sprache in Europa.",
        "de-DE-KatjaNeural"
    ),
    "spanish.wav": (
        "Hola. El español es uno de los idiomas más hablados del mundo.",
        "es-ES-ElviraNeural"
    ),
    "italian.wav": (
        "Ciao. L'italiano è una lingua melodiosa e culturale.",
        "it-IT-ElsaNeural"
    ),
    "portuguese.wav": (
        "Olá. O português é falado em vários países.",
        "pt-BR-FranciscaNeural"
    ),
    "russian.wav": (
        "Здравствуйте. Русский язык широко используется.",
        "ru-RU-SvetlanaNeural"
    ),
    "chinese.wav": (
        "你好。中文是世界上使用人数最多的语言。",
        "zh-CN-XiaoxiaoNeural"
    ),
    "japanese.wav": (
        "こんにちは。日本語は美しい言語です。",
        "ja-JP-NanamiNeural"
    ),
    "korean.wav": (
        "안녕하세요. 한국어는 체계적인 언어입니다.",
        "ko-KR-SunHiNeural"
    ),
    "arabic.wav": (
        "مرحبا. اللغة العربية من أقدم لغات العالم.",
        "ar-SA-ZariyahNeural"
    ),
    "turkish.wav": (
        "Merhaba. Türkçe zengin bir dildir.",
        "tr-TR-EmelNeural"
    ),
    "thai.wav": (
        "สวัสดี ภาษาไทยเป็นภาษาที่ไพเราะ",
        "th-TH-PremwadeeNeural"
    ),
    "vietnamese.wav": (
        "Xin chào. Tiếng Việt là ngôn ngữ giàu bản sắc.",
        "vi-VN-HoaiMyNeural"
    ),
    "indonesian.wav": (
        "Halo. Bahasa Indonesia mudah dipelajari.",
        "id-ID-GadisNeural"
    ),
    "swahili.wav": (
        "Habari. Kiswahili ni lugha maarufu Afrika.",
        "sw-KE-ZuriNeural"
    ),
    "dutch.wav": (
        "Hallo. Nederlands wordt gesproken in Nederland.",
        "nl-NL-ColetteNeural"
    ),
    "polish.wav": (
        "Cześć. Język polski jest językiem słowiańskim.",
        "pl-PL-AgnieszkaNeural"
    ),
}

async def main():
    for filename, (text, voice) in voices.items():
        try:
            print(f"🔊 Generating {filename}")
            await edge_tts.Communicate(text, voice).save(filename)
            await asyncio.sleep(1)  # ✅ prevent rate limit
        except Exception as e:
            print(f"⚠️ Skipped {filename}: {e}")

    print("\n✅ All available audios generated successfully!")

asyncio.run(main())
