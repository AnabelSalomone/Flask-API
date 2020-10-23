import requests

BASE = "http://127.0.0.1:5000/"

album_name = input("Enter the name of the album: ")
num = input("Song number you wish to know: ")

format_album_name = album_name.replace(" ", "+")

response = requests.get(BASE + "album/" + format_album_name + "/" + num)
print(response.json())
