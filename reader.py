import threading
import psycopg2
import time

# Function for retrieving&marking messages as received for db
def read_and_mark_messages(db_server, sender_name):
    conn = psycopg2.connect(db_server)  # Connect to the database
    cursor = conn.cursor()

    while True:
        cursor.execute("SELECT record_id, sender_name, message, sent_time FROM async_messages WHERE received_time IS NULL AND sender_name != %s FOR UPDATE", (sender_name,))
        message = cursor.fetchone()

        if message:
            record_id, sender, msg, sent_time = message
            print(f"Sender {sender} sent '{msg}' at time {sent_time}.")
            cursor.execute("UPDATE async_messages SET received_time = %s WHERE record_id = %s", (time.strftime('%Y-%m-%d %H:%M:%S'), record_id))
            conn.commit()

    cursor.close()
    conn.close()