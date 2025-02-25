ARG BUILD_FROM=ghcr.io/hassio-addons/base-python:latest
FROM $BUILD_FROM

WORKDIR /app

# Kopiere das Python-Skript und eine evtl. benötigte Konfigurationsdatei
COPY udp_to_mqtt.py /app/udp_to_mqtt.py
COPY config.json /app/config.json

# Installiere die Python-Abhängigkeiten
RUN pip install --no-cache-dir paho-mqtt

# Starte das Skript
CMD ["python3", "/app/udp_to_mqtt.py"]
