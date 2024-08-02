from elevenlabs import play
from elevenlabs.client import ElevenLabs
from pydub import AudioSegment
import os
import warnings

# Initialize the ElevenLabs client
client = ElevenLabs(api_key="YOUR_API_KEY")

#
# Resolve the warning
warnings.filterwarnings("ignore", message=".*protected_namespaces.*")

# Define speaker voices
voices = {
    "사회자": "gISMLrFD8OURC8emf0yJ",
    "철수": "dtzTfYBOfRiqaWUI80lQ",
    "수민": "Anhs1G2NoOIK6y5MdRmB",
}


# Step 1: Read the text file
def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    return lines


# Step 2: Parse the text into a list of [speaker, content]
def parse_text(lines):
    parsed_lines = []
    for line in lines:
        if ":" in line:
            speaker, content = line.split(":", 1)
            parsed_lines.append([speaker.strip(), content.strip()])
    return parsed_lines


# Step 3: Generate audio for each line
def generate_audio(parsed_lines):
    audio_files = []
    for speaker, content in parsed_lines:
        voice_id = voices.get(speaker)
        if not voice_id:
            raise ValueError(f"Unknown speaker: {speaker}")

        audio = client.generate(
            text=content, voice=voice_id, model="eleven_multilingual_v2"
        )

        file_name = f"{speaker}_{content[:10]}.mp3"
        with open(file_name, "wb") as f:
            for chunk in audio:
                f.write(chunk)
        audio_files.append(file_name)
    return audio_files


# Step 4: Combine audio files into one
def combine_audio(audio_files, output_file):
    combined = AudioSegment.empty()
    for file in audio_files:
        audio_segment = AudioSegment.from_file(file)
        combined += audio_segment
    combined.export(output_file, format="mp3")


# Main function to execute all steps
def main(input_text_file, output_audio_file):
    lines = read_text_file(input_text_file)
    parsed_lines = parse_text(lines)
    audio_files = generate_audio(parsed_lines)
    combine_audio(audio_files, output_audio_file)

    # Clean up individual audio files
    for file in audio_files:
        os.remove(file)


# Example usage
if __name__ == "__main__":
    main("토론스크립트.txt", "final_output.mp3")
