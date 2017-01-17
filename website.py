import requests
import hashlib


class Website:

    def __init__(self, url, period):
        self.url = url
        self.period = period
        self.hashcode = ''

    def get_period(self):
        return self.period

    def get_url(self):
        return self.url

    def set_hashcode(self, hashcode):
        self.hashcode = hashcode

    def check_update(self):
        try:
            request = requests.get(self.url)
        except requests.exceptions.RequestException as exc:
            print("Could not connect to", self.url)
            return False
        currenthash = hashlib.sha256(request.text.encode('utf-8')).hexdigest()
        if currenthash != self.hashcode:
            self.hashcode = currenthash
            return True
        else:
            return False
