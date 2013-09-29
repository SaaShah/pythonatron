'''
Facillitates loosely coupled communication between objects. 
Example: 
    m1 = Message('message_1')
    r1 = Receiver()
    r2 = Receiver()

    r1.register(m1.name)
    r2.transmit(m1) # All relays registered to m1.name will receive this message

Message objects can have data attached to them and be treated as named dto objects.
Example:
    m1.data = {0: 'Hello', 1: 'World'}
    r2.transmit(m1)

The data attahced to m1 is now sent to all relays registered to m1.name.
'''

relays = {}

def add_relay(relay, message_name):
    if relays.has_key(message_name) is False:
        relays[message_name] = set() 
    relays[message_name].add(relay)

def transmit(message):
    if relays.has_key(message.name):
        for relay in relays[message.name]:
            relay.receive(message)

def remove_relay(relay, message_name):
    if relays.has_key(message_name):
        if relay in relays[message_name]:
            relays[message_name].remove(relay)

class Relay(object):
    def __init__(self):
        self.name = 'relay'
        self.message_names = set()

    def receive(self, message):
        # Override with sub class
        pass

    def register(self, message_name):
        self.message_names.add(message_name)
        add_relay(self, message_name)

    def transmit(self, message):
        message.origin = self
        transmit(message)

    def unregister(self, message_name):
        self.message_names.remove(message_name)
        remove_relay(self, message_name)

    def unregister_all(self):
        for name in self.message_names:
            remove_relay(self, name)
        self.message_names.clear()

    def __str__(self):
        return 'Relay: ' + self.name

class Message(object):
    def __init__(self, name='message'):
        self.name = name 
        self.origin = None

