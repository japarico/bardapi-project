from bardapi import Bard
import os
import requests

os.environ['_BARD_API_KEY'] = ''

session = requests.Session()

session.headers = {
    "Host": "bard.google.com",
    "X-Same-Domain": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Origin": "https://bard.google.com",
    "Referer": "https://bard.google.com/",
}

session.cookies.set("__Secure-1PSID", os.getenv("_BARD_API_KEY"))

bard = Bard(token=os.getenv("_BARD_API_KEY"), session=session, timeout=30)

def read_file(filename):
    """Reads the contents of a file and returns it as a string."""
    with open(filename, "r") as f:
        return f.read()

contents = read_file("data/data.txt")
print(bard.get_answer("Please summarize the following text." + contents)['content'])
