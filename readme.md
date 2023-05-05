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
- Once the Docker container is running, you can run commands below to see how OpenAI can help data curation.
  - Convert timestamp string into a certain format
    - "docker exec -it python-app-openai-demo python example_1.py"
  - Get sentiment of the text
    - "docker exec -it python-app-openai-demo python example_2.py"
  - Extract mentioned to user ID from the free text
    - "docker exec -it python-app-openai-demo python example_3.py"
