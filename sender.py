import threading
import time
import psycopg2
import random
import json

# Function to insert a message into the database
def insert_message(message, sender_name, conn):
    sent_time = time.strftime('%Y-%m-%d %H:%M:%S')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO async_messages (sender_name, message, sent_time) VALUES (%s, %s, %s)", (sender_name, message, sent_time))
    conn.commit()

# Prompt the user for database details
db_name = input("Enter the database name: ")
db_user = input("Enter the database user: ")
db_password = input("Enter the database password: ")

# Store the details of the database in a configuration file
config = {
    "db_name": db_name,
    "db_user": db_user,
    "db_password": db_password
}

with open('config.json', 'w') as config_file:
    json.dump(config, config_file)

# Database server IP 
db_server_ips = ['127.0.0.1']
connections = []
threads = []

# Connections to database server
for ip in db_server_ips:
    conn = psycopg2.connect(
        host=ip,
        database=db_name,
        user=db_user,
        password=db_password,
        port="5432"
    )
    connections.append(conn)

sender_name = 'Tural'  # Showing the Sender Name

# Function to send messages
def sender_thread(connect):
    while True:
        message = input("Enter your message (or type 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        insert_message(message, sender_name, connect)

# Create sender threads for each DB server
sender_threads = []
for conn in connections:
    thread = threading.Thread(target=sender_thread, args=(conn,))
    sender_threads.append(thread)
    thread.start()

# Wait for sender threads to finish
for thread in sender_threads:
    thread.join()

# It will shut down connections when process is finished
for conn in connections:
    conn.close()