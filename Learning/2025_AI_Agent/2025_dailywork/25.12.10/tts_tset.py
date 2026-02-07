from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

speech = client.audio.speech.create(
    model="gpt-4o-mini-tts",
    voice="alloy",
    input="반갑습니다. VS Code에서 음성이 나오도록 테스트를 진행하고 있습니다"
)

with open("output.mp3", "wb") as f:
    f.write(speech.content)
