from threading import Timer
import time


class Checker(object):

    def __init__(self):
        self.sites = []
        self.iteration = 0

    def add_site(self, site):
        self.sites.append(site)

    def remove_site(self, site):
        self.sites.remove(site)

    def check_sites(self):
        for site in self.sites:
            if self.iteration % site.get_period() == 0:
                if site.check_update() and self.iteration != 0:
                    print(time.strftime("%H:%M"), site.get_url(), "has changed!")
        self.iteration += 1

    def run(self):
        t = Timer(60.0, self.run)
        t.start()
        self.check_sites()
