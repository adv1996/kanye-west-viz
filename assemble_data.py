import requests
import time
import csv

artist_id = '5K4W6rqBFWDnAN6FQUkS6x' # kanye west's artist's id
# api token expires every couple of hours
token = 'Bearer {insert token}'
headers = {'Content-Type': 'appplication/json',
    'Authorization': token}
allData = []
allData.append(
  ['id', 'album', 'name', 'danceability', 'energy', 'key', 'loudness', 'speechiness', 'acounticness', 
    'instrumentalness', 'liveness', 'valence', 'tempo', 'duration'
  ]
)
music_map = {}
library = {}
num_requests = 0
def getSpotifyData(artist_id, artistName):
  url = 'https://api.spotify.com/v1/artists/'+ artist_id + '/albums'
  # tokens expire need to find when they expire
  r = requests.get(url, headers=headers)
  data = r.json()
  for album in data['items']:
    if album['album_type'] == 'album':
      library[album['name']] = (album['name'], album['release_date'], album['total_tracks'], album['id'])
      print(album['name'], album['release_date'], album['total_tracks'], album['id'])
  # after getting each album we need to create a map with each id and then we need to get the tracks for each album
  # after getting each song we need to get each song's attributes
  for album in library.values():
    getSongFromAlbum(album[3], album[0])
    time.sleep(5)
  return library

def getSongFromAlbum(id, album_name):
  # could use get several albums instead to reduce number of requests sent
  album_url = 'https://api.spotify.com/v1/albums/' + id + '/tracks?limit=25'
  tracks = requests.get(album_url, headers=headers)
  track_data = tracks.json()
  lookupSongs = ''
  for track in track_data['items']:
    # print(track)
    music_map[track['id']] = (track['name'], album_name)
    print(track['id'], track['name'], track['duration_ms'], track['track_number'])
    lookupSongs = track['id'] + ',' + lookupSongs
  getSongAttributes(lookupSongs)

def getSongAttributes(ids):
  # take a list of ids and make into a id1,id2,..,idx format no spaces between ids
  joined_songs = ids
  tracks_url = 'https://api.spotify.com/v1/audio-features?ids=' + joined_songs
  track_attributes = requests.get(tracks_url, headers=headers)
  attr_data = track_attributes.json()
  for song in attr_data['audio_features']:
    assembleData(song)

def assembleData(song):
  song_id = song['id']
  song_name = music_map[song_id][0]
  song_album = music_map[song_id][1]
  danceability = song['danceability']
  energy = song['energy']
  song_key = song['key']
  loudness = song['loudness']
  speechiness = song['speechiness']
  acousticness = song['acousticness']
  instrumentalness = song['instrumentalness']
  liveness = song['liveness']
  valence = song['valence']
  tempo = song['tempo']
  duration_ms = song['duration_ms']
  song_data = [song_id, song_album, song_name, danceability, energy, song_key, loudness, speechiness,
    acousticness, instrumentalness, liveness, valence, tempo, duration_ms]
  allData.append(song_data)
  print('ADDED Song ', len(allData))

def saveData():
  getSpotifyData(artist_id, 'Kanye West')
  saveToCSV('kanye_west.csv', allData)

def saveToCSV(filename, data):
  with open(filename, 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(data)
  csvFile.close()
  print('Completed Web Scraping ' + str(len(data)) + ' Items')
  print('Kanye West Songs Added')

saveData()