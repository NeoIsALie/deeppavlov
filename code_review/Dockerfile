FROM python:3.10-slim
WORKDIR /usr/src/app
COPY . ./
RUN apt-get update && apt-get install tar
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN tar zxfv data.tgz
ENTRYPOINT ["python", "csv_sum.py"]
