from elevenlabs import play
from elevenlabs.client import ElevenLabs

client = ElevenLabs(
api_key="YOUR_API_KEY", # Defaults to ELEVEN_API_KEY
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

위 코드를 고려해서 아래 작업을 하는 파이썬 코드를 작성해줘

1단계 : 텍스트파일을 파이썬에서 읽어와서 인식

2단계 : 텍스트파일을 [”발화자”, “발화내용”] 형태로 리스트로 표현해주기

3단계 : 리스트의 발화 내용을 하나씩 순차적으로 돌면서, 발화자에 해당하는 음성을 만들기

4단계 : 각각 만들어진 음성파일 최종본 하나로 합치기

사회자 : dtzTfYBOfRiqaWUI80lQ

철수 : pNInz6obpgDQGcFmaJgB

수민 : cjVigY5qzO86Huf0OWal

샘플 텍스트파일은 다음과 같아
사회자: 안녕하세요 여러분, 오늘의 토론 주제는 “생성형 AI는 세상을 얼마나 바꿀 것인가?“입니다. 철수와 수민이 각자의 의견을 가지고 토론을 벌일 예정입니다. 먼저 철수의 의견을 들어보겠습니다.

철수: 안녕하세요. 저는 생성형 AI가 세상을 혁명적으로 바꿀 것이라고 생각합니다. 첫째, 생성형 AI는 콘텐츠 제작에서 큰 변화를 일으킬 것입니다. 현재 AI는 글쓰기, 음악 작곡, 그림 그리기 등 다양한 예술 분야에서 사람과 같은 수준의 창작물을 만들어내고 있습니다. 이러한 기술은 창작의 장벽을 낮추고 누구나 쉽게 콘텐츠를 만들 수 있게 도와줄 것입니다.

수민: 반갑습니다. 철수의 의견에 일부 동의하지만, 저는 생성형 AI의 한계도 분명하다고 생각합니다. AI가 창작물을 만드는 데 도움을 줄 수는 있지만, 인간의 창의성과 감성을 완전히 대체할 수는 없습니다. 예를 들어, 인간의 경험과 감정이 담긴 작품은 AI가 따라오기 힘든 부분이죠. AI는 도구로서 유용하지만, 그것이 인간의 역할을 완전히 대체할 수는 없을 것입니다.
