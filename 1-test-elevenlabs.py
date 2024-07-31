from elevenlabs import play
from elevenlabs.client import ElevenLabs

client = ElevenLabs(
    api_key="YOUR_API_KEY",  # Defaults to ELEVEN_API_KEY
)
korean_text = "안녕하세요 너의 이름은 뭐니"
audio = client.generate(
    text=korean_text,
    voice="pNInz6obpgDQGcFmaJgB",
    model="eleven_multilingual_v2",
)

with open("audio3.mp3", "wb") as f:
    for chunk in audio:
        f.write(chunk)
