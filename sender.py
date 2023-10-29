import threading
import time
import psycopg2

# Function for inserting messages -> to the database
def insert_message(conn, sender_name, message):
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO async_messages (sender_name, message, sent_time) VALUES (%s, %s, %s)", (sender_name, message, current_time))
    conn.commit()
    cursor.close()

# Function to send messages
def sender_thread(db_server, sender_name):
    conn = psycopg2.connect(db_server)  # Connect to the database
    while True:
        message = input("Enter your message (or type 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        insert_message(conn, sender_name, message)
    conn.close()