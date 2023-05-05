FROM python:3.10
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN mkdir /root/.kaggle
RUN cp kaggle.json "/root/.kaggle"
RUN sh setup.sh
