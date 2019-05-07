import json
import csv

def convert():
  csvFile = open('/Users/advaith/Projects/Visualizations/kanye-west/src/data/kanye_west.csv')
  reader = csv.DictReader(csvFile, fieldnames=('id','album','name','danceability','energy','key','loudness','speechiness','acousticness','instrumentalness','liveness','valence','tempo','duration'))
  out = json.dumps([ row for row in reader ])
  jsonFile = open('kanye_west.json', 'w')
  jsonFile.write(out)

convert()