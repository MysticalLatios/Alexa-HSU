#Code modified from http://www.cyber-omelette.com/2017/01/alexa-run-script.html

#Aws import
import boto3

#system imports
import os
import time

#Our pachages imports
import spcontroler
import secrets


#Keys for amazon cloud services
access_key = secrets.access_key
access_secret = secrets.access_secret
region = secrets.region
queue_url = secrets.queue_url

def pop_aws_que(client, url):
    response = client.receive_message(QueueUrl = url, MaxNumberOfMessages = 8)

    #Oldest message is pulled?
    message = response['Messages'][0]['Body']
    receipt = response['Messages'][0]['ReceiptHandle']
    client.delete_message(QueueUrl = url, ReceiptHandle = receipt)
    return message
    
client = boto3.client('sqs', aws_access_key_id = access_key, aws_secret_access_key = access_secret, region_name = region)

waittime = 20
client.set_queue_attributes(QueueUrl = queue_url, Attributes = {'ReceiveMessageWaitTimeSeconds': str(waittime)})

time_start = time.time()
while (time.time() - time_start < 300):
        print("Checking...")
        try:
                message = pop_aws_que(client, queue_url)
                print(message)
                if message == "Pon":
                    spcontroler.click_power_on()
                elif message == "Poff":
                    spcontroler.click_power_off()
                elif message == "Deskstop":
                    spcontroler.input_comp_1()
                elif message == "Laptop":
                    spcontroler.input_comp_2()
        except:
            pass