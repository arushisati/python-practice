# notification_polymorphism.py

class Notification:
    def send(self):
        print("Sending notification")

class Email(Notification):
    def send(self):
        print("Email Sent")

class SMS(Notification):
    def send(self):
        print("SMS Sent")

class WhatsApp(Notification):
    def send(self):
        print("WhatsApp Message Sent")

notifications = [Email(), SMS(), WhatsApp()]

for n in notifications:
    n.send()
