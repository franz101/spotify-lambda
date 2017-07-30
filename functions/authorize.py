import os

from requests_oauthlib import OAuth2Session

from functions import spotify_helpers as spot

if __name__ == "main":
    """ interactive authorizaton helper """
    client_id = os.getenv('SPOTIFY_CLIENT_ID')
    client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

    # a bogus redirect uri
    redirect_uri = "https://localhost.deadheaven.com/uri"

    # the scope required for our API requests
    scope = r'user-read-recently-played'

    # Request URLs for Spotify
    request_authorization_url = "https://accounts.spotify.com/authorize"
    request_token_url = "https://accounts.spotify.com/api/token"


    # Create our client.
    oauth = OAuth2Session(client_id=client_id,
                          scope=scope,
                          redirect_uri=redirect_uri)

    authorization_url, state = oauth.authorization_url(request_authorization_url)

    print('Go to %s and authorize access.' % authorization_url)

    authorization_response = input('Psate the full returedn URL here: ')

    token = oauth.fetch_token(
        request_token_url,
        client_secret=client_secret,
        authorization_response=authorization_response)

    spot.save_token(token)