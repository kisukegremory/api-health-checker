from requests import get, Response
from requests.exceptions import ConnectionError
import logging


class Listener:
    """Runs a request instead of store the response

    :param sess_method:
        uses a requests.get/requests.post to watch and endpoint.
    :param \**kwargs: 
        Optional arguments that ``request`` takes, 
        as example: the url.
    """
    def __init__(self,sess_method=get,**kwargs):
        self.method = sess_method
        self.kwargs = kwargs
    def run(self) -> Response:
        try:
            return self.method(**self.kwargs)
        except ConnectionError:
            logging.critical("No Internet Available")