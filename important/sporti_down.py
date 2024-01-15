import requests

url = "https://latest-spotify-downloader.p.rapidapi.com/track/2gAKyzcfFIlMYdJ2b836At"

headers = {
	"X-RapidAPI-Key": "5feee309f4msh888c1c19ad08363p103bc4jsnc59a54ff9f3d",
	"X-RapidAPI-Host": "latest-spotify-downloader.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())