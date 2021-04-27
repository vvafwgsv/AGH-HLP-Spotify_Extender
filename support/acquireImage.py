import os
from requests import get


class AcquireImage:
    def __init__(self, url, name):
        if not is_saved(name):
            self.response = get(url)
            self.file = open("./images/" + name, "w+b")

            self.file.write(self.response.content)
            self.file.close()


def get_path(name):
    return "./images/" + name


def is_saved(name):
    # print(os.getcwd())
    if name in os.listdir("./images/"):
        return True
    return False
