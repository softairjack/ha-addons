import socket
import json
import paho.mqtt.client as mqtt

# Konfiguration
UDP_IP = "0.0.0.0"  # Empfängt Daten auf allen Interfaces
UDP_PORT = 22222     # Port, den dein Gerät nutzt
MQTT_BROKER = "homeassistant.local"  # Passe ggf. die IP/Adresse an
MQTT_TOPIC = "udp/data"

# MQTT Client einrichten
mqtt_client = mqtt.Client()
mqtt_client.connect(MQTT_BROKER, 1883, 60)

# UDP-Socket einrichten
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"🔹 UDP Listener gestartet auf {UDP_IP}:{UDP_PORT}")

while True:
    data, addr = sock.recvfrom(1024)  # 1024 Bytes empfangen
    message = data.decode("utf-8")  # Falls die Daten als Text kommen
    print(f"📥 Empfangene Daten: {message} von {addr}")

    # Versuche die Daten als JSON zu interpretieren
    try:
        json_data = json.loads(message)
        mqtt_client.publish(MQTT_TOPIC, json.dumps(json_data))
        print(f"✅ Gesendet an MQTT: {json_data}")
    except json.JSONDecodeError:
        print("⚠️ Keine gültigen JSON-Daten empfangen")

