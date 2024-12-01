#Python base image
FROM python:3.10

#working directory
WORKDIR /app
COPY mqtt_reader.py /app/mqtt_reader.py
RUN pip install gmqtt
EXPOSE 1884
CMD ["python", "mqtt_reader.py"]
