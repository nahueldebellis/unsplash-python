import webbrowser
import requests

unsplash = requests.get('https://api.unsplash.com/photos/random/?client_id=c3e972e14c88e82b61ad9def94f4705ed116f6bc7d3bf82c08c35e17de75e1ef')
un = unsplash.json()
webbrowser.open(un['urls']['raw'])
