from endpoint_listener import Listener
from datetime import datetime

class EndpointWatcher:
    def __init__(self,listener:Listener):
        self.listener = listener

    def watch(self):
        res = self.listener.run()
        return {
            'url':res.url,
            'status_code':res.status_code,
            'elapsed_time':res.elapsed.total_seconds(),
            'created':datetime.now()
        }