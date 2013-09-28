receivers = {}

def add_receiver(receiver, message):
    if receivers.has_key(message) is False:
        receivers[message] = []
    receivers[message].append(receiver)

def transmit(message):
    if receivers.has_key(message):
        for receiver in receivers[message]:
            receiver.receive(message)

class Receiver(object):

    def register(self, message):
        add_receiver(self, message)

    def transmit(self, message):
        transmit(message)

    def receive(self, message):
        pass

class MyReceiver(Receiver):
    def __init__(self):
        Receiver.__init__(self)
        self.transmit('message_a')
        
if __name__ == '__main__':
    MESSAGE_A = 'message_a'
    MESSAGE_B = 'message_b'

    r1 = Receiver()
    r1.register(MESSAGE_A)

    r2 = MyReceiver()


