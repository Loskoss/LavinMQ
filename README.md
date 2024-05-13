# LavinMQ RabbitMQ Producer-Consumer Setup

This repository contains code for setting up a producer-consumer architecture using RabbitMQ messaging broker, specifically tailored for LavinMQ.

## Prerequisites
Before running the code, make sure you have:

- Access to a LavinMQ Online account
- Basic understanding of RabbitMQ concepts, including exchanges, bindings, and routing keys

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/Loskoss/LavinMQ.git
    ```

2. Install dependencies:
    ```bash
    pip install pika
    ```

3. Set up environment variables:
   - Create a `.env` file with the following content:
     ```plaintext
     CLOUDAMQP_URL=<your_lavinmq_url>
     ```
     Replace `<your_lavinmq_url>` with your LavinMQ Online URL.

## Usage

### Producer
1. Ensure you have set up the environment variables with your LavinMQ URL in the `.env` file.
2. Run the producer script:
    ```bash
    python producer.py
    ```
    The producer will connect to the RabbitMQ server specified in the environment variables, send messages to the queue, and then exit after a specified timeout.

### Consumer
1. Ensure you have set up the environment variables with your LavinMQ URL in the `.env` file.
2. Run the consumer script with command line arguments
    ```bash
    python consumer.py <user_group>
    ```
   Replace `<user_group>` with the desired user group (e.g., engineering, sales, finance). The consumer will connect to the RabbitMQ server, listen for messages in the queue corresponding to the provided user group, process them, and acknowledge them after processing.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.
