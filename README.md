<div align="center">
  <h1 style="font-family: 'Times New Roman', serif; color: #2E86C1; font-size: 2.5em;">🚀 LavinMQPROJECT</h1>
  <p style="font-family: 'Times New Roman', serif; font-style: italic; color: #566573;">Empowering Slack notifications with LavinMQ</p>
</div>

## 📝 About
This project is a part of MLH Data Week given by LavinMQ. It's about building a basic notification system for Slack channels.

## ⚙️ Requirements
In order to create this project or use this project preview on your computer, it is a must to log in to CloudAMQP.

As CloudAMQP provides servers for LavinMQ and RabbitMQ. So it is a must!!
After creating an account, you have to create a LavinMQ instance. You can refer to this guide -> [LavinMQ Guide](https://hackp.ac/ghwdata24-lavinmq-guide2)

And this code works only when the LavinMQ instance is created and you are using the instance URL (indirectly we can say that this code only works when there is an internet connection and your CloudAMQP website is open in your browser and the instance should be created).

## 📋 Overview
This project consists of three challenges

### 🎯 Challenge 1: Creating the producer and consumer
This challenge consists of creating a producer which sends a message ("HELLO WORLD") to the LavinMQ server and a consumer which receives a message from the LavinMQ server.
#### 📄 Output
1. After downloading the zip file, unzip it, open the folder in your preferred IDE which supports Python. Make sure that Python is installed on your computer.
2. Also install `pika` and `python_dotenv` packages.
3. Now copy your instance URL from your CloudAMQP website and modify it in the place of CloudAMQP URL in the code.
4. Both in `hello_world_producer.py` and `hello_world_consumer.py` files. 
5. Now open two terminals simultaneously and make sure that you are in the challenge1 repository or navigate it using the `cd` command.
6. In terminal 1 enter this command `python hello_world_consumer.py` and in terminal 2 enter this `python hello_world_producer.py`.
   If everything goes well, you should get the following output in the different terminals.
   
   <h3>Terminal 1 - Consumer <h3>
     
    ![output of consumer](https://github.com/pranav2910/LavinMQPROJECT/assets/77099940/2b02aa99-06a8-4c5f-855c-31c83dbf525b)
   
   <h3>Terminal 2 - Producer <h3>
     
    ![output of producer](https://github.com/pranav2910/LavinMQPROJECT/assets/77099940/3a2675f8-b6e7-4037-9bba-6b5ee758bea0)

### 🚧 Challenge 2: Creating queues, exchanges and bindings
This challenge consists of creating exchanges, bindings and routing keys in LavinMQ — building on the concepts you’ve learnt in the previous challenge.
You will modify the producer you created in the previous challenge to fit the requirements of the notification system.
- First, you will create a direct exchange `slack_notifications` and three queues: `hr_queue, marketing_queue, and support_queue` in the producer.
- Then bind each queue to the `slack_notifications` exchange using the corresponding binding keys: `hr, marketing, and support` respectively.
- Next, simulate a scenario where the producer publishes events from the `hr, marketing, and support` Slack channels with the routing keys `hr, marketing, and support` respectively.
- Using the bindings and routing keys above, the `slack_notifications` exchange will route messages from the `hr, marketing, and support` Slack channels to the `hr_queue, marketing_queue, and support_queue` queues respectively.
#### 📄 Output
1. Repeat the first three steps of challenge 1.
2. Modify the URL in the "direct_exchange_consumer.py" and also in "direct_exchange_producer.py".
3. Open 4 terminals simultaneously. In the first three terminals, run three instances of your consumer application with:

Terminal 1 - a consumer instance for hr messages: `python direct_exchange_consumer.py hr`

Terminal 2 - a consumer instance for support messages: `python direct_exchange_consumer.py support`

Terminal 3 - a consumer instance for marketing messages: `python direct_exchange_consumer.py marketing`

In the fourth terminal, run your producer application with: `python direct_exchange_producer.py`

If everything goes well, you should get the following output in the different terminals.

  <h3>Terminal 1 - hr consumer</h3>

  ![Screenshot 2024-05-13 022058](https://github.com/pranav2910/LavinMQPROJECT/assets/77099940/470b2848-c8dc-4e9c-97cf-f37195c5b4e2)
  

  <h3>Terminal 2 - support</h3>
  
  ![Screenshot 2024-05-13 022033](https://github.com/pranav2910/LavinMQPROJECT/assets/77099940/831b7d93-bc8f-4965-8183-9cf4dadc6ff7)

  
  <h3>Terminal 3 - marketing</h3>
  
  ![Screenshot 2024-05-13 022020](https://github.com/pranav2910/LavinMQPROJECT/assets/77099940/03d66d7c-1163-4c6a-bca7-90dfdceb31ac)

  <h3>Terminal 4 - Producer</h3>
  
  ![Screenshot 2024-05-13 022005](https://github.com/pranav2910/LavinMQPROJECT/assets/77099940/7b7f3394-f453-4fe3-9b28-567cf516ae96)


### 🏆 Challenge 3: Running three consumers
This challenge consists of creating 1-to-1 mapping between queues and consumers.

You will modify the consumer you created in the first challenge to fit the requirements of the notification system.

As we have three queues we will be needing three consumers. Creating a script from scratch for each consumer will be redundant. Instead, modify your existing consumer script to accept command line arguments.

Modify the consumer script to accept one of three command line arguments: `hr, marketing, and support`

The consumer will then bind to the `hr_queue, marketing_queue, or support_queue` at runtime, depending on the argument passed.
#### 📄 Output
1. Repeat the first three steps of challenge 1.
2. Modify the URL in the "direct_exchange_consumer.py" and also in "direct_exchange_producer.py".
3. Open 4 terminals simultaneously. In the first three terminals, run three instances of your consumer application with:

Terminal 1 - a consumer instance for hr messages: `python direct_exchange_consumer.py hr`

Terminal 2 - a consumer instance for support messages: `python direct_exchange_consumer.py support`

Terminal 3 - a consumer instance for marketing messages: `python direct_exchange_consumer.py marketing`

In the fourth terminal, run your producer application with: `python direct_exchange_producer.py`

If everything goes well, you should get the following output in the different terminals.

  <h3>Terminal 1 - hr consumer</h3>

  ![Screenshot 2024-05-13 022921](https://github.com/pranav2910/LavinMQPROJECT/assets/77099940/bb6e253e-6892-4317-8eff-e82d39bcd946)


  
  <h3>Terminal 2 - support</h3>

  ![Screenshot 2024-05-13 022907](https://github.com/pranav2910/LavinMQPROJECT/assets/77099940/2849d500-565a-4fe4-aedc-d7515cd5003f)

  
  <h3>Terminal 3 - marketing</h3>

  ![Screenshot 2024-05-13 022855](https://github.com/pranav2910/LavinMQPROJECT/assets/77099940/20cab509-91cf-4750-8614-366cd0732ce7)

  
  <h3>Terminal 4 - producer</h3>

  ![Screenshot 2024-05-13 022843](https://github.com/pranav2910/LavinMQPROJECT/assets/77099940/9926da4e-03ff-477b-a6e4-0179301e9584)


</div>
