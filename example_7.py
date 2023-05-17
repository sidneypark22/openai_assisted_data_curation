import os
from dotenv import load_dotenv
from langchain.agents import create_spark_dataframe_agent, create_pandas_dataframe_agent
from langchain.llms import OpenAI
import datetime
import pandas as pd

load_dotenv()

pd_df = pd.read_csv('room_booked_status.csv')
# If verbose is True, it will reveal how the agent come up with an answer.
agent = create_pandas_dataframe_agent(OpenAI(temperature=0), pd_df, verbose=False)

### Based on findings, dataframe structure i.e. column names, data types and values and questions need to be fine tuned together
### to get better answers
agent.run("Is there a room available for 6 guests to stay for 2 nights from 28 May 2023 and what is the price in total?")
agent.run("Which room is the most popular and least popular?")

### Agent Query Results were as below:

"""
>>> agent.run("Is there a room available for 6 guests to stay for 2 nights from 28 May 2023 and what is the price in total?")
'Yes, there is a room available for 6 guests to stay for 2 nights from 28 May 2023 and the total price is 800.'
>>> agent.run("Is there a room available for 6 guests to stay for 2 nights from 28 May 2023 and what is the price in total?")
'The room is available for 6 guests to stay for 2 nights from 28 May 2023 and the total price is 800.'
>>> agent.run("Is there a room available for 6 guests to stay for 2 nights from 28 May 2023 and what is the price in total?")
'The room is available for 6 guests to stay for 2 nights from 28 May 2023 and the total price is 800.'
>>> agent.run("Which room is the most popular?")
'Room 1 is the most popular.'
>>> agent.run("Which room is the most popular and least popular?")
'Room 1 is the most popular and Room 3 is the least popular.'
"""

### Probabaly can try with Spark as below. But it seemed langchain worked more smoothly with Pandas dataframe.
spark = SparkSession.builder.getOrCreate()
spark_df = spark.read.option('inferSchema', 'True').option('header', 'True').csv('room_booked_status.csv')
spark_df.printSchema()
spark_df.show()

spark_agent = create_spark_dataframe_agent(llm=OpenAI(temperature=0), df=spark_df, verbose=False)

agent.run("Is there a room available for 6 guests to stay for 2 nights from 28 May 2023 and what is the price in total?")
agent.run("Which room is the most popular and least popular?")
