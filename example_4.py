import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

model_id = 'whisper-1'

media_file_path = 'output_jin.wav'
media_file = open(media_file_path, 'rb')

response = openai.Audio.transcribe(
    model=model_id,
    file=media_file,
)
ahjahjajalkjalskdjasd
print(response.text)
