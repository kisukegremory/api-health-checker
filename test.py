from unittest import TestCase, main
from requests import Response
from src.endpoint_listener import Listener

class TestFirstTrial(TestCase):

    def test_listener_exceptions(self):
        ep = Listener(url="https://viacep.com.br/ws/01001000/json/")
        res = ep.run()
        self.assertIsInstance(res, Response)
    



if __name__ == '__main__':
    main()