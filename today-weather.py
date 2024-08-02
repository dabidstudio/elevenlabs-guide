from elevenlabs.client import ElevenLabs
from openai import OpenAI

# OpenAI API key
perplexity_api_key = "YOUR_OPENAI_API_KEY"
eleven_api_key = "YOUR_ELEVENLABS_API_KEY"


# Function to get today's weather in Seoul
def get_weather():
    query = "오늘은 며칠이지? 나는 서울에 있어, 오늘 날씨를 알려줘 기온은 몇도지?"

    client = OpenAI(api_key=perplexity_api_key, base_url="https://api.perplexity.ai")
    response = client.chat.completions.create(
        model="llama-3-sonar-large-32k-online",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": query},
        ],
    )
    return response.choices[0].message.content


# Function to generate and save audio
def generate_audio(text):
    client = ElevenLabs(api_key=eleven_api_key)
    audio = client.generate(
        text=text,
        voice="pNInz6obpgDQGcFmaJgB",
        model="eleven_multilingual_v2",
    )
    with open("weather_update.mp3", "wb") as f:
        for chunk in audio:
            f.write(chunk)


# Get weather information
weather_info = get_weather()

# Generate audio from weather information
generate_audio(weather_info)

print("Weather information:", weather_info)
print("Audio file 'weather_update.mp3' has been created.")
