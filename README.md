# LavinMQPROJECT

# About
This project is a part of MLH data week which was give by LavinMq to complete it. 
this project is about building a basic notification system , which notifies people about what events happening in  slack channel that they belong to.

# Requirements
In order to create this project or use this project prewiew in your computer, it is must to login into CloudAMQP.

As cloudAMQP provides servers for lavinMQ and rabbitMQ. So it is must!!
After creating an account you have to create an LavinMQ instance, you can refer to this guide -> https://hackp.ac/ghwdata24-lavinmq-guide2

And this code works only when the LavinMQ instace is created and you are using the instance url(indirectly we can say that this code only works when there is internet connection and your CloudAMQP website is open in you browser and instance should be created).

# Overview
This project consist of three challenges
# challenge 1
This clallenge consists of creating a producer which sends a message("HELLO WORLD") to the LavinMQ server and a consumer which receives message from the lavinMQ server.
 # output
 1. After downloding the zip file unzip it , open the folder in your prefered IDE which 
    supports python, Make sure that python is installed in your computer.
 2. Now copy your instance url from your cloud AMQP website and modify it in the palce of CloudAMQP url in the code. Both in hello_world_producer.py and hello_world_consumer.py files. 
 3. Now open two teriminal simultaniously and make sure that you are in challenge1 repository or navigate it using "cd" command.
 4. In terminal1 enter this command "python hello_world_consumer.py" and in terminal2 enter this "python hello_world_producer.py". 
    
# challenge 2
This challenge consists of creating
