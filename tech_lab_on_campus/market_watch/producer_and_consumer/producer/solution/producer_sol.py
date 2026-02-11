from producer_interface import mqProducerInterface
import pika
import os

class mqProducer(mqProducerInterface):
    def __init__(self, routing_key:str, exchange_name:str) -> None:
        self.routing_key = routing_key
        self.exchange_name = exchange_name
        connection = self.setupRMQConnection()

    
    def setupRMQConnection(self) -> None:
        con_params = pika.URLParameters(os.environ["AMQP_URL"])
        self.connection = pika.BlockingConnection(parameters=con_params)
        self.channel = self.connection.channel()
        message = "HI"
        self.publishOrder(message)

    def publishOrder(self, message: str) -> None:
        self.channel.basic_publish(
            exchange= self.exchange_name,
            routing_key= self.routing_key,
            body= message
        )
        self.channel.close()
        self.connection.close()

'''
setupRMQConnection Function: Establish connection to the RabbitMQ service.
publishOrder: Publish a simple UTF-8 string message from the parameter.
publishOrder: Close Channel and Connection.

class mqProducerInterface:
    def __init__(self, routing_key: str, exchange_name: str) -> None:
        # Save parameters to class variables

        # Call setupRMQConnection
        pass

    def setupRMQConnection(self) -> None:
        # Set-up Connection to RabbitMQ service

        # Establish Channel

        # Create the exchange if not already present

        pass

    def publishOrder(self, message: str) -> None:
        # Basic Publish to Exchange

        # Close Channel

        # Close Connection
    
        pass
'''    