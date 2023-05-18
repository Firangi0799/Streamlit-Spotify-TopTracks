import streamlit as st
import base64
from requests import post, get
import json
import urllib.parse


# Spotify API credentials
client_id = "0c4e52cbb9af433d831b1b98f3503a1f"
client_secret = "fefb383f0d544ec48d3deb4a701c94ff"

# Get the access token
def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

# Get the headers
def get_headers(token):
    return {"Authorization": "Bearer " + token}

# Search for an artist
def search_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_headers(token)
    query_params = {
        "q": artist_name,
        "type": "artist",
        "limit": 1
    }
    query = urllib.parse.urlencode(query_params)

    query_url = url + "?" + query

    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]
    if len(json_result) == 0:
        st.write("Artist not found. Please enter the correct spelling of the artist's name.")
        return None

    return json_result[0]

# Get the top 10 songs by an artist
def get_top_songs(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=IN"
    headers = get_headers(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)
    tracks = json_result.get("tracks")
    if not tracks:
        st.write("No tracks found.")
        return None

    return tracks

# Create a Streamlit app
st.set_page_config(page_title="Spotify Top 10 Songs", page_icon=":musical_note:", layout="centered", initial_sidebar_state="expanded")

# Get the user input
artist_name = st.text_input("Enter an artist name:")

# If the user enters a name, get the top 10 songs
if artist_name:
    # Get the artist ID
    artist = search_artist(get_token(), artist_name)
    if artist:
        artist_id = artist["id"]

        # Get the top 10 songs
        songs = get_top_songs(get_token(), artist_id)

        # Display the songs
        if songs:
            for idx, song in enumerate(songs):
                st.write(f"{idx + 1}. {song['name']}", style="font-size: 18px")
