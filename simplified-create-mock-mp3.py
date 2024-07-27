import uuid
from dotenv import load_dotenv
import os
from elevenlabs.client import ElevenLabs

load_dotenv()

# Initialize the client
client = ElevenLabs(api_key=os.environ["ELEVENLABS_API_KEY"])

# Dialogue text
dialogue_text = """
지수: 안녕하세요, 민혁씨. 요즘 잘 지내세요?
민혁: 안녕하세요, 지수씨. 네, 잘 지내고 있습니다. 지수씨는요?
지수: 저도 잘 지내고 있어요. 오늘 이야기하고 싶은 주제가 있는데, 바로 생성 AI의 미래에 대해서입니다.
민혁: 아, 생성 AI요? 정말 흥미로운 주제네요. 어떤 부분이 궁금하신가요?

"""

# Parse the dialogue text
dialogues = dialogue_text.strip().split("\n")

# Initialize a list to hold the audio data
audio_clips = []

# Process each line of the dialogue
for dialogue in dialogues:
    speaker, text = dialogue.split(": ", 1)
    voice = "Chris" if speaker == "지수" else "Charlie"
    # Generate the audio
    audio_generator = client.generate(
        text=text, voice="Chris", model="eleven_multilingual_v2"
    )

    # Convert the generator to bytes
    audio_data = b"".join(audio_generator)

    # Append the audio data to the list
    audio_clips.append(audio_data)

# Concatenate all the audio clips into one audio file
final_audio = b"".join(audio_clips)

# Generate a unique file name for the output MP3 file
save_file_path = f"{uuid.uuid4()}.mp3"

# Save the final audio to a file
with open(save_file_path, "wb") as f:
    f.write(final_audio)

print(f"Audio file generated and saved as '{save_file_path}'.")
