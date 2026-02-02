import torch
import soundfile as sf
from transformers import AutoModel

# Use CPU
device = torch.device("cpu")

# Load IndicF5 model
model = AutoModel.from_pretrained(
    "ai4bharat/IndicF5",
    trust_remote_code=True
)
model = model.to(device)
model.eval()

text = "வணக்கம், இது ஒரு சோதனை"

# Depending on repo version, the function may be tts() or infer()
with torch.no_grad():
    try:
        wav, sr = model.tts(text=text, lang="ta")
    except AttributeError:
        # Some versions use infer()
        wav, sr = model.infer(text=text, lang="ta")

# Save output
sf.write("output.wav", wav, sr)
print("✅ Audio generated successfully: output.wav")
