from myapp.tests import *

class TestMaincontrollerController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='mainController', action='index'))
        assert 'Home' in response

    def test_users(self):
        response = self.app.get(url(controller='mainController', action='users', userid='derek'))
        assert 'User' in response
