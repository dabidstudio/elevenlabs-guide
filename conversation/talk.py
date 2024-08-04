import os

from elevenlabs.client import ElevenLabs
from pydub import AudioSegment
from pydub.playback import play

# ElevenLabs API 초기화
client = ElevenLabs(api_key="")

# 음성 모델 ID
voice_ids = {
    "사회자": "dtzTfYBOfRiqaWUI80lQ",
    "철수": "pNInz6obpgDQGcFmaJgB",
    "수민": "cjVigY5qzO86Huf0OWal",
}


# 텍스트 파일 읽기
def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.readlines()


# 텍스트 파일을 리스트로 변환
def parse_text(lines):
    dialogues = []
    for line in lines:
        if ":" in line:
            speaker, content = line.split(":", 1)
            dialogues.append([speaker.strip(), content.strip()])
    return dialogues


# 발화 내용을 음성으로 생성
def generate_audio(dialogues):
    audio_segments = []
    for speaker, content in dialogues:
        voice_id = voice_ids.get(speaker, voice_ids["사회자"])
        audio = client.generate(
            text=content,
            voice=voice_id,
            model="eleven_multilingual_v2",
        )
        audio_file_path = f"{speaker}.mp3"
        with open(audio_file_path, "wb") as f:
            for chunk in audio:
                f.write(chunk)
        audio_segment = AudioSegment.from_mp3(audio_file_path)
        audio_segments.append(audio_segment)
        os.remove(audio_file_path)  # 임시 파일 삭제
    return audio_segments


# 생성된 음성 파일 합치기
def merge_audio(audio_segments, output_path):
    combined = AudioSegment.empty()
    for segment in audio_segments:
        combined += segment
    combined.export(output_path, format="mp3")


# 메인 함수
def main():
    file_path = "토론스크립트.txt"
    output_path = "토론결과.mp3"

    lines = read_text_file(file_path)
    dialogues = parse_text(lines)
    audio_segments = generate_audio(dialogues)
    merge_audio(audio_segments, output_path)
    print(f"Final audio saved as {output_path}")


if __name__ == "__main__":
    main()
