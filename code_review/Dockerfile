# Only the RUN, COPY, and ADD instructions create layers.
# Следовательно, минимизируем количество RUN в файле
FROM python:3.10-slim
COPY . /usr/src/app
RUN apt-get update && \
    apt-get install tar && \
    tar zxfv /usr/src/app/data.tgz &&\
    pip install -r /usr/src/app/requirements.txt
ENTRYPOINT ["python", "/usr/src/app/csv_sum.py"]