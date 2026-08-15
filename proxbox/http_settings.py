import requests
from requests.adapters import HTTPAdapter

class TimeoutHTTPAdapter(HTTPAdapter):
    def __init__(self, *args, **kwargs):
        self.timeout = kwargs.pop('timeout', 5)
        super().__init__(*args, **kwargs)

    def send(self, request, **kwargs):
        kwargs['timeout'] = self.timeout
        return super().send(request, **kwargs)

def custom_http_session(timeout=5):
    adapter = TimeoutHTTPAdapter(timeout)
    session = requests.Session()
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    
    return session