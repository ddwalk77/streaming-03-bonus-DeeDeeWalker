# streaming-03-bonus-DeeDeeWalker
Custom bonus project on decoupling with a message broker

Name: DeeDee Walker

Date: 1/24/23

Original data: https://www.kaggle.com/datasets/jimschacko/airlines-dataset-to-predict-a-delay

Project description:

The data set is a record of flights from kaggle that consist of an identifier for the set of data on the filerow, airline, type of aircraft, airport from, airport To, day of the week as a #, time, length of flight, and a delay indicator as a 0 or 1. The producer.py file imports the cvs file, reads each row, assigning it to a message string. A connection to RabbitMQ is established and the message string is pulled in to send. The consumer.py file is set to read the messages as they come through. The data that was collected in the csv file is being sent to the consumer via the producer so the data can be processed. 

Producer terminal:
![Producer terminal script](https://github.com/ddwalk77/streaming-03-bonus-DeeDeeWalker/blob/main/bonusproducer.png "Producer terminal script")
Consumer terminal:
![Consumer terminal script](https://github.com/ddwalk77/streaming-03-bonus-DeeDeeWalker/blob/main/bonusconsumer.png "Consumer terminal script")
