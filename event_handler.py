class EventEmitter:
    def __init__(self):
        self.events = {}

    def on(self, event_name, handler):
        self.events[event_name] = handler

    def emit(self, event_name, *args):
        if event_name in self.events:
            self.events[event_name](*args)

emitter = EventEmitter()