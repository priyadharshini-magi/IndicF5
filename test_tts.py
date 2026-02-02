# import os
# import numpy as np
# import soundfile as sf
# import torch

# # Disable torch.compile on Windows CPU
# torch.compile = lambda model, *args, **kwargs: model

# from transformers import AutoModel

# # ── Config ─────────────────────────────────────────
# repo_id = "ai4bharat/IndicF5"
# device = torch.device("cpu")
# output_file = "output.wav"

# # Simple Tamil text
# text_to_speak = "நான் தமிழ் பேசுகிறேன்"

# # Optional reference audio (can improve style)
# ref_audio_path = "prompts/PAN_F_HAPPY_00001.wav"
# ref_text = "This is a sample reference transcript that matches the reference audio"

# # ── Load Model ─────────────────────────────────────
# print("Loading IndicF5 model...")
# model = AutoModel.from_pretrained(repo_id, trust_remote_code=True)
# model = model.to(device).eval()
# print("✅ Model loaded successfully!")

# # ── Check reference audio file exists ─────────────
# if not os.path.isfile(ref_audio_path):
#     raise FileNotFoundError(
#         f"Reference audio not found: {ref_audio_path}\n"
#         "Make sure you have a prompt WAV file in the 'prompts' folder"
#     )

# # ── Generate Speech ────────────────────────────────
# print("Generating speech...")

# # Use model directly for TTS
# try:
#     audio_out = model(text=text_to_speak, ref_audio_path=ref_audio_path, ref_text=ref_text)
# except Exception as e:
#     print("Error generating audio:", e)
#     exit(1)

# # Convert to numpy if torch tensor
# if isinstance(audio_out, torch.Tensor):
#     audio = audio_out.detach().cpu().numpy()
# elif isinstance(audio_out, np.ndarray):
#     audio = audio_out
# else:
#     audio = np.array(audio_out)

# # Normalize if needed
# if audio.dtype == np.int16:
#     audio = audio.astype(np.float32) / 32768.0

# # ── Save WAV ───────────────────────────────────────
# sf.write(output_file, audio, samplerate=24000)
# print(f"✅ Audio saved to {output_file}")


# install dependencies first
# pip install TTS soundfile

from TTS.api import TTS

# ── Config ─────────────────────────────────────────
output_file = "output.wav"
text_to_speak = "நான் தமிழ் பேசுகிறேன்"

# ── Load a ready-to-use Tamil TTS model ───────────
# This is a pre-trained model, ready for inference
tts = TTS(model_name="kushalv1/indic-tts-tamil")

# ── Generate speech ────────────────────────────────
tts.tts_to_file(text=text_to_speak, file_path=output_file)

print(f"✅ Audio saved to {output_file}")
