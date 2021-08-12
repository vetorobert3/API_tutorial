import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 1000, "name": "Idiots in Cars", "views": 100000},
        {"likes": 782, "name": "Cat Dance", "views": 12355584},
        {"likes": 187121, "name": "How to make a video", "views": 100000},
        {"likes": 10, "name": "Tim eats pizza", "views": 10},]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.get(BASE + "video/6")
print(response.json())