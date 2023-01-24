"""
Name: DeeDee Walker
Date: 1/24/23

Listens for messages on the queue.
This process runs continously. 

Approach
---------
Simple - one producer / one consumer.

Since this process runs continuously, 
if we want to emit more messages, 
we'll need to open a new terminal window.

"""

# add imports at the beginning of the file
import pika
import sys
import csv

# Declare a variable to hold the output file name
output_file_name = "consumer.csv"

# Create a file object for output (w = write access)
# On Windows, without newline='', 
# we'll get an extra line after each record
output_file = open(output_file_name, "w", newline='')

# Create a csv writer for a comma delimited file
writer = csv.writer(output_file, delimiter=",")

#Define the host
hn = 'localhost'

#define the queue
queue = 'airline'

# define a callback function to be called when a message is received
def process_message(ch, method, properties, body):
        """ Define behavior on getting a message."""
        print(" [x] Received %r" % body.decode())
        # put the values in a list (see the square brackets)
        # and write the list of values to the output file
        writer.writerow([body])

# define a main function to run the program
def main():
    """Main program entry point."""
    
    # when a statement can go wrong, use a try-except block
    try:
        # try this code, if it works, keep going  
        # create a blocking connection to the RabbitMQ server
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=hn))

    # except, if there's an error, do this
    except Exception as e:
        print()
        print("ERROR: connection to RabbitMQ server failed.")
        print(f"Verify the server is running on host={hn}.")
        print(f"The error says: {e}")
        print()
        sys.exit(1)

    try: 
        # use the connection to create a communication channel
        channel = connection.channel()

        # use the channel to declare a queue
        channel.queue_declare(queue)

        # use the channel to consume messages from the queue
        channel.basic_consume(queue, on_message_callback=process_message, auto_ack=True)

        # print a message to the console for the user
        print(" [*] Waiting for messages. To exit press CTRL+C")

        # start consuming messages via the communication channel
        channel.start_consuming()

    # except, in the event of an error OR user stops the process, do this
    except Exception as e:
        print()
        print("ERROR: something went wrong.")
        print(f"The error says: {e}")
        output_file.close()
        sys.exit(1)
    except KeyboardInterrupt:
        print()
        print(" User interrupted continuous listening process.")
        output_file.close()
        sys.exit(0)
    finally:
        print("\nClosing connection. Goodbye.\n")
        connection.close()

# Standard Python idiom to indicate main program entry point
# This allows us to import this module and use its functions
# without executing the code below.
# If this is the program being run, then execute the code below
if __name__ == "__main__":
    main()
  
     
