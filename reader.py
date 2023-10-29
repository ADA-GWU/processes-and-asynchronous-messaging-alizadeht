import threading
import psycopg2
import time
import psycopg2
import json

# Function to retrieve&mark messages -> received
def read_and_mark_messages(db_server, sender_name):
    cursor = conn.cursor()

    while True:
        cursor.execute("SELECT record_id, sender_name, message, sent_time FROM async_messages WHERE received_time IS NULL AND sender_name != %s FOR UPDATE", (sender_name,))
        message = cursor.fetchone()

        if message:
            record_id, sender, msg, sent_time = message
            print(f"Sender {sender} sent '{msg}' at time {sent_time}.")
            cursor.execute("UPDATE async_messages SET received_time = %s WHERE record_id = %s", (time.strftime('%Y-%m-%d %H:%M:%S'), record_id))
            conn.commit()

    conn.close()

# Load the database details from the configuration file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

db_name = config['db_name']
db_user = config['db_user']
db_password = config['db_password']

# Database server IP 
db_server_ips = ['127.0.0.1']
connections = []

sender_name = 'Tural'  # Sender Name

# Connections to database server
for ip in db_server_ips:
    conn = psycopg2.connect(
        host=ip,
        database=db_name,
        user=db_user,
        password=db_password
    )
    connections.append(conn)
