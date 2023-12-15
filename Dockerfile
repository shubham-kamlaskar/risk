FROM python:3.10-slim-buster
COPY . /app
WORKDIR /app
EXPOSE 5000
ENV NAME world
RUN apt update -y && apt install awscli -y
RUN pip install --upgrade pip
RUN pip install --upgrade scikit-learn flask numpy
RUN pip install -r requirements.txt

CMD ["python","risk.py"]
