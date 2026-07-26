from abc import ABC, abstractmethod


class NotificationChannel(ABC):

    @abstractmethod
    def send(self,message):
        pass



class EmailChannel(NotificationChannel):

    def __init__(self,server):

        self.server=server


    def send(self,message):

        print(
            f"Email via {self.server}: {message}"
        )



class SMSChannel(NotificationChannel):

    def __init__(self,number):

        self.number=number


    def send(self,message):

        print(
            f"SMS {self.number}: {message}"
        )



class NotificationService:

    def __init__(self):

        self.channels=[]


    def add_channel(self,channel):

        self.channels.append(channel)


    def notify_all(self,message):

        for channel in self.channels:

            channel.send(message)