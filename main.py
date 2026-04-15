### SET API KEY ACCORDINGLY TO YOUR SETUP. I reccomend this (copy the following to a linux terminal): sudo apt install pwgen ; pwgen 64 1 ###

import requests as req
import os
import json
url = "https://kontent.longnecksoftware.ch/" # My own website. Change this to accomodate you needs. (Dont forget the slash!!!)
header = {"x-api-key": "foo"} # Example. DO NOT USE THIS IN PROD. Change this to accomodate you needs.

def main(url, header):
    isPlaying = False # Maybe I'll use this. To check if music is playing.
  
    if os.path.isdir(".cache") == False:
        os.mkdir(".cache")

    if os.path.exists("./.cache/list.txt") == False:
        f = open("./.cache/list.txt", "w")
        print("Downloading the list...")
        x = req.get(url + "get-data", headers = {header})
        f.write(x.text)
        f.close()
        x.text


def dl_song(uid, url, header, extension):
    with req.get(url + f"get-music?song_id={uid}", headers = header, stream=True) as r:
        r.raise_for_status()
        with open(f".cache/{uid}.{extension}", 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)

def refresh_list(url, header):
    f = open("./.cache/list.txt", "w")
    print("Downloading the list...")
    x = req.get(url + "get-data", headers = {header})
    f.write(x.text)
    f.close()
    return x.text

# start execution. nothing to run for now just testing with functions
if 1 == 1:
    pass
