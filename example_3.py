import os
from dotenv import load_dotenv
import openai
import polars as pl

pl.Config.set_fmt_str_lengths(500)

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
csv_file_path = './twcs/twcs.csv'

def ask_openai_text_task(question, question_data):
    print(f"""{question}: {question_data}""")
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

question = "From this tweet, return the user the tweet is mentioned to with @ sign if it is missing"

df = pl.read_csv(csv_file_path).limit(3)

df = df.with_columns(
    pl.col('text').apply(
        lambda x: ask_openai_text_task(
            question=question,
            question_data=f'"{x}"'
        )
    ).alias("new_col_openai")
)

print(df)
