import requests

with open('input.txt') as inf:
    r = requests.get(inf.readline().strip())
    print(len(r.text.splitlines()))
