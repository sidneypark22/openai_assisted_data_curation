import os
from dotenv import load_dotenv
import openai
import polars as pl

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
csv_file_path = './twcs/twcs.csv'

def ask_openai_text_task(question, question_data):
    #print(f"""{question}: {question_data}""")
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"""{question}: {question_data}""",
        temperature=0,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    response_text = [i for i in response.choices[0].text.split('\n') if i != '']
    return response_text[0]

question = "Convert this to YYYY-MM-DD HH24:MI:SS format please"

df = pl.read_csv(csv_file_path).limit(3)

df = df.with_columns(
    pl.col('created_at').apply(
        lambda x: ask_openai_text_task(
            question=question,
            question_data=x
        )
    ).alias("new_col_openai")
)

print(df.select("tweet_id", "created_at", "text", "new_col_openai"))
