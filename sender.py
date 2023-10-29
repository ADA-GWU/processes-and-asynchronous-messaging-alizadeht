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
