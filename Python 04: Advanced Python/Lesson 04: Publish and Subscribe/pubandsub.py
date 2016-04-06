class Publisher:
    def __init__(self):
        self.subscribers =  []
    
    def subscribe(self, subscriber):
        if subscriber in self.subscribers:
            raise ValueError("Multiple subscriptions are not allowed")
        self.subscribers.append(subscriber)
        
    def unsubscribe(self, subscriber):
        if subscriber not in self.subscribers:
            raise ValueError("Can only unsubscribe subscribers")
        self.subscribers.remove(subscriber)
        self.subscribers[0](str(subscriber).split()[-1].replace('>',''))
        
    def publish(self, s):
        """
        Use a 'copy' of self.subscribers to stop skipping.  But don't use the 
        first element which is a registered function.
        """
        for subscriber in self.subscribers[1:]:
            subscriber(s)
    
if __name__ == "__main__":
    def announcer(s):
        print("*** '{}' has been unsubscribed. ***".format(s))
        
    class SimpleSubscriber:
        def __init__(self, name, publisher):
            self.name = name
            publisher.subscribe(self.process)
            """
            Keep track of call to the process method on a per instance level.
            """
            self.process_count = 0
            
        def process(self, s):
            print(self.name, ":", s.upper())
            """ 
            Because the check is done after processing, the last call will
            be the third one.  No point in updating the counter, then checking.
            """
            if self.process_count == 2:
                """
                Using 'self.process', which is the same key as for subscribing,
                continues to allow registering the callable method directly,
                instead of registering an instance and then calling a specific method.
                This then allows registering arbitrary functions to the publisher.
                """
                publisher.unsubscribe(self.process)
            else:
                self.process_count += 1
            
        def __repr__(self):
            return self.name
            
    publisher = Publisher()
    publisher.subscribe(announcer)
    for i in range(6):
        newsub = SimpleSubscriber("Sub"+str(i), publisher)
        line = input("Input {}: ".format(i))
        publisher.publish(line)
            