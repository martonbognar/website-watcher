import requests


class Website(object):

    def __init__(self, url, period):
        self.url = url
        self.period = period

    def get_period(self):
        return self.period

    def check_update(self):
        request = requests.get(self.url)
        print(self.url)
        print("\tEtag: ", request.headers.get('Etag', "No Etag"))
        print("\tLast-Modified: ", request.headers.get('Last-Modified', "No Last-Modified"))
