import threading
import psycopg2
import time
import json

# Function to retrieve&mark messages -> received
def read_and_mark_messages(conn, sender_name):
    cursor = conn.cursor()

    while True:
        cursor.execute("SELECT record_id, sender_name, message, sent_time, received_time FROM async_messages WHERE received_time IS NULL AND sender_name != %s FOR UPDATE", (sender_name,))
        text = cursor.fetchone()

        if text:
            record_id, sender, msg, sent_time = text
            received_time = time.strftime('%Y-%m-%d %H:%M:%S')
            print(f"Sender {sender} sent '{msg}' at time {sent_time}.")

            cursor.execute("UPDATE async_messages SET received_time = NOW() WHERE record_id = %s", (record_id,))



    conn.commit()
    time.sleep(1)


# Load the database details from the configuration file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

db_name = config['db_name']
db_user = config['db_user']
db_password = config['db_password']

# Database server IP 
db_server_ips = ['127.0.0.1']
connections = []

sender_name = 'Tural'  # Showing the Sender Name

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

# Create reader threads for each DB server
reader_threads = []
for conn in connections:
    thread = threading.Thread(target=read_and_mark_messages, args=(conn, sender_name))
    reader_threads.append(thread)
    thread.start()

    # Wait for user input to stop
print("Press 'e' and enter to exit.")
while True:
    user_input = input()
    if user_input.lower() == 'e':
        break

# Wait for reader threads to finish
for thread in reader_threads:
    thread.join()

# It will shut down connections when process is finished
for conn in connections:
    conn.close()
