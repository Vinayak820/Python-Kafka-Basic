from kafka import KafkaConsumer

# Configuration variables
KAFKA_TOPIC = "demo-topic"
KAFKA_SERVER = "localhost:9092"

def consume_from_kafka():
    """Consumes messages from Kafka and processes them."""
    # Initialize KafkaConsumer
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_SERVER,
        auto_offset_reset='earliest',
        enable_auto_commit=True
    )

    print("Waiting for messages...")
    # Consume messages in an infinite loop
    for message in consumer:
        # Decode the byte value back into a string (email)
        email = message.value.decode("utf-8")
        print(f"New SignUp with Email: {email}")

if __name__ == "__main__":
    # Ensure you have the 'kafka-python' library installed: pip install kafka-python
    consume_from_kafka()
