# OpenAI assisted data curation

There are cases where it is tricky to transform data due to complexity of data e.g. free text.

We can ask OpenAI to do such unusual data trasnformations.

In order to run this, you need to have a Docker installed.

## How to:

- Clone this repo
- Go to Kaggle, create API key, then place the kaggle.json file in the folder.
- Go to OpenAI, create API key, then place the API key into the file ".env" with the variable name "OPENAI_API_KEY".
- Install Docker
- Build a Docker image using the command: "docker build -t python-app-openai-demo ."
- Run a Docker container using the image built above using the command: "docker run --name python-app-openai-demo -d -it python-app-openai-demo"
- Once the Docker container is running, you can run commands below to see how OpenAI can help data curation. The OpenAI curated data is placed in "new_col_openai" column.
  - Convert timestamp string into a certain format
    - Question asked: "Convert this to YYYY-MM-DD HH24:MI:SS format please"
    - "docker exec -it python-app-openai-demo python example_1.py"
┌──────────┬────────────────────────────────┬───────────────────────────────────┬─────────────────────┐
│ tweet_id ┆ created_at                     ┆ text                              ┆ new_col_openai      │
│ ---      ┆ ---                            ┆ ---                               ┆ ---                 │
│ i64      ┆ str                            ┆ str                               ┆ str                 │
╞══════════╪════════════════════════════════╪═══════════════════════════════════╪═════════════════════╡
│ 1        ┆ Tue Oct 31 22:10:47 +0000 2017 ┆ @115712 I understand. I would li… ┆ 2017-10-31 22:10:47 │
│ 2        ┆ Tue Oct 31 22:11:45 +0000 2017 ┆ @sprintcare and how do you propo… ┆ 2017-10-31 22:11:45 │
│ 3        ┆ Tue Oct 31 22:08:27 +0000 2017 ┆ @sprintcare I have sent several … ┆ 2017-10-31 22:08:27 │
└──────────┴────────────────────────────────┴───────────────────────────────────┴─────────────────────┘

  - Get sentiment of the text
    - Question asked: "Rate the sentiment in this tweet from 0 to 10"
    - "docker exec -it python-app-openai-demo python example_2.py"
┌──────────┬────────────────────────────────┬───────────────────────────────────┬────────────────┐
│ tweet_id ┆ created_at                     ┆ text                              ┆ new_col_openai │
│ ---      ┆ ---                            ┆ ---                               ┆ ---            │
│ i64      ┆ str                            ┆ str                               ┆ str            │
╞══════════╪════════════════════════════════╪═══════════════════════════════════╪════════════════╡
│ 1        ┆ Tue Oct 31 22:10:47 +0000 2017 ┆ @115712 I understand. I would li… ┆ 10             │
│ 2        ┆ Tue Oct 31 22:11:45 +0000 2017 ┆ @sprintcare and how do you propo… ┆ ?              │
│ 3        ┆ Tue Oct 31 22:08:27 +0000 2017 ┆ @sprintcare I have sent several … ┆ 3              │
└──────────┴────────────────────────────────┴───────────────────────────────────┴────────────────┘

  - Extract mentioned to user ID from the free text
    - Question asked: "From this tweet, return the user the tweet is mentioned to with @ sign if it is missing"
    - "docker exec -it python-app-openai-demo python example_3.py"
┌──────────┬────────────────────────────────┬───────────────────────────────────┬────────────────┐
│ tweet_id ┆ created_at                     ┆ text                              ┆ new_col_openai │
│ ---      ┆ ---                            ┆ ---                               ┆ ---            │
│ i64      ┆ str                            ┆ str                               ┆ str            │
╞══════════╪════════════════════════════════╪═══════════════════════════════════╪════════════════╡
│ 1        ┆ Tue Oct 31 22:10:47 +0000 2017 ┆ @115712 I understand. I would li… ┆ @115712        │
│ 2        ┆ Tue Oct 31 22:11:45 +0000 2017 ┆ @sprintcare and how do you propo… ┆ @SprintCare    │
│ 3        ┆ Tue Oct 31 22:08:27 +0000 2017 ┆ @sprintcare I have sent several … ┆ @sprintcare    │
└──────────┴────────────────────────────────┴───────────────────────────────────┴────────────────┘


# Langchain answer questions based on dataframe

Langchain makes it easier to do more exciting things more easily by using OpenAI model.

In this example, I tried creating a dataset with accommodation rooms and their booking status to show availabilities.

The sample dataset created is room_booked_status.csv.

This is in the example_7.py file.

It required fine tuning of dataset including column names, data types and data values and the questions to derive more correct and better answers.

Below are answers provided by the agent powered with OpenAI API for qu
>>> agent.run("Is there a room available for 6 guests to stay for 2 nights from 28 May 2023 and what is the price in total?")
'The room is available for 6 guests to stay for 2 nights from 28 May 2023 and the total price is 800.'
>>> agent.run("Which room is the most popular?")
'Room 1 is the most popular.'
>>> agent.run("Which room is the most popular and least popular?")
'Room 1 is the most popular and Room 3 is the least popular.'


# OpenAI Whisper to dictate speech

I asked my son to say anything and record his speech. By using whisper OpenAI model, I was able to convert the speech into textx - surprisingly it captured everything I said quitely next to my son as well.

This is in the example_4.py file.

My idea is to convert the question spoken into text then ask the question to OpenAI via API i.e. ask a question via voice then get an answer.

However, I've reached my API rate limit and I cannot do more demo on this XD
