from kafka import KafkaProducer
import time
import os

# Configuration variables
KAFKA_TOPIC = "demo-topic"
KAFKA_SERVER = "localhost:9092"
EMAIL_FILE = "emails.txt"

def send_to_kafka():
    """Continuously checks for new emails and sends them to Kafka."""
    # Initialize producer without a value_serializer, so we manually encode the value later
    producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
    seen_emails = set()

    while True:
        if os.path.exists(EMAIL_FILE):
            with open(EMAIL_FILE, "r", encoding="utf-8") as file:
                for email in file:
                    email = email.strip()
                    if email and email not in seen_emails:
                        # Value is manually encoded to bytes as shown in the image
                        producer.send(KAFKA_TOPIC, email.encode("utf-8"))
                        print(f"Sent email {email} to Kafka topic {KAFKA_TOPIC}")
                        seen_emails.add(email)

        time.sleep(2) # Check for new emails every 2 seconds

    # These lines are inside the function but outside the infinite loop, as shown in the image.
    producer.flush()
    producer.close()

if __name__ == "__main__":
    send_to_kafka()
