# Spotify Top 10 Songs

This is a Streamlit app that allows you to search for an artist and retrieve their top 10 songs from Spotify.

## Deployment

The project is deployed and accessible at [https://spotify-toptracks.onrender.com](https://spotify-toptracks.onrender.com).

## Installation

To run this application locally, you need to have Python installed. Clone the repository and install the required dependencies using the following commands:

```shell
git clone https://github.com/Firangi0799/Streamlit-Spotify-TopTracks.git
pip install -r requirements.txt
```

## Usage

To use the app, follow these steps:

1. Obtain Spotify API credentials:
   - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and create a new application.
   - Retrieve the Client ID and Client Secret.
2. Set up the credentials:
   - Replace the `client_id` and `client_secret` variables in the code with your own credentials.
3. Run the app:
   - Execute the following command in the terminal:
     ```shell
     streamlit run app.py
     ```
4. Enter an artist name:
   - In the Streamlit app, you will see a text input field. Enter the name of the artist you want to search for.
5. View the top 10 songs:
   - After entering the artist name, the app will display the top 10 songs by that artist, if available.

## How it works

This app uses the Spotify Web API to search for artists and retrieve their top songs. Here's an overview of the key components:

- `get_token()`: This function retrieves the access token from the Spotify API using your client credentials (Client ID and Client Secret).
- `get_headers(token)`: This function returns the headers required for making API requests, including the access token.
- `search_artist(token, artist_name)`: This function searches for an artist by name using the Spotify API and returns the first result.
- `get_top_songs(token, artist_id)`: This function retrieves the top 10 songs by an artist using the Spotify API, based on the artist's ID.
- Streamlit app:
  - The app uses Streamlit to create a simple user interface.
  - It prompts the user to enter an artist name using a text input field.
  - When the user submits the artist name, the app calls the `search_artist()` function to retrieve the artist's information.
  - If the artist is found, the app calls the `get_top_songs()` function to retrieve their top 10 songs.
  - Finally, the app displays the top songs in a numbered list.

## Notes

- This app is designed to retrieve top songs for artists in India (`country=IN`). If you want to search for artists from a different country, modify the `country` parameter in the `get_top_songs()` function.
- If the artist is not found or no tracks are available, appropriate error messages will be displayed in the app.

Feel free to explore and modify the code to suit your needs!
