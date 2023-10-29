[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/qg4qXfSB)



Hello, this is the second assignment for the Principles of Distributed Systems. The concept is about implementation of the asynchronous concurrent messaging. Therefore, I wrote a sender and reader software that reads the list of Database server IPs. It connected to all the DBs in different threads.  
In the sender software, created threads equal to the DB servers, and request user's input. Every time the user enters a text, it chose one of the threads and inserts a record into ASYNC_MESSAGE table with SENDER_NAME , entered message and current_time.
In the reader software, checked available messages in each DB. Avail message is the one that has (RECEIVED_TIME IS NULL and SENDER_NAME != yours).


How to install: download as a zip file from GitHub.

To run the code: open the terminal(2 windows, 1 for reader, 1 for sender) For each window, write the code below:

P.S: cd filepath is a must!

e.g: cd /Users/turalalizada/Desktop/processes-and-asynchronous-messaging-alizadeht

You can compile the code and run the application on any OS.

1. sender:
 python sender.py (if you have macOS, try python3 sender.py)
2. reader:
 python reader.py (if you have macOS, try python3 reader.py)


You have to enter the details of the database in sender.py as shown below:
<img width="567" alt="image" src="https://github.com/ADA-GWU/processes-and-asynchronous-messaging-alizadeht/assets/78111301/eb173bbb-ab38-44bb-b999-d4865795bc17">

After that, informations about the database will be sent to JSON file:
<img width="633" alt="image" src="https://github.com/ADA-GWU/processes-and-asynchronous-messaging-alizadeht/assets/78111301/85c7b000-6fe6-481b-8c52-7b896647c742">

Then, write something you want, and see that message in the database:
<img width="830" alt="image" src="https://github.com/ADA-GWU/processes-and-asynchronous-messaging-alizadeht/assets/78111301/81c0a1ef-c309-4215-9e67-d435e6ef5a81">

   
