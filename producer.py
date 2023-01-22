"""
    This program sends a message to a queue on the RabbitMQ server from a csv file read.

    Name: DeeDee Walker
    Date: 1/22/23

"""

# add imports at the beginning of the file
import pika
import sys
import csv
import time

# read from a file to get some fake data - declaring variable input_file
input_file = open("airlines.csv", "r")

# Create a csv reader for a comma delimited file
reader = csv.reader(input_file, delimiter=",")

#Declare the name of the queue & host
queue_name = airline
host= localhost

try:
    for row in reader:
        # read a row from the file
        id, Airline, Flight, AirportFrom, AirportTo, DayofWeek, Time, Length, Delay = row

        # use an fstring to create a message from our data
        # notice the f before the opening quote for our string?
        fstring_message = f"[{id}, {Airline}, {Flight}, {AirportFrom}, {AirportTo}, {DayofWeek}, {Time}, {Length}, {Delay}]"

        # prepare a binary (1s and 0s) message to stream
        MESSAGE = fstring_message.encode()

        # sleep for a few seconds
        time.sleep(3)
    
        try:
            # create a blocking connection to the RabbitMQ server
            conn = pika.BlockingConnection(pika.ConnectionParameters(host))
            # use the connection to create a communication channel
            ch = conn.channel()
            # use the channel to declare a queue
            ch.queue_declare(queue=queue_name)
            # use the channel to publish a message to the queue
            ch.basic_publish(exchange="", routing_key=queue_name, body=MESSAGE)
            # print a message to the console for the user
            print(f" [x] Sent {MESSAGE}")
        except pika.exceptions.AMQPConnectionError as e:
            print(f"Error: Connection to RabbitMQ server failed: {e}")
            sys.exit(1)
        finally:
            # close the connection to the server
            conn.close()
except KeyboardInterrupt:
    # close the file objects to release the resources
    input_file.close()
