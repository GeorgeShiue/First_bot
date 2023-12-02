import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
from flask import Flask, request, url_for, session, redirect

app = Flask(__name__)

app.config['SESSION_COOKIE_NAME'] = 'Spotify Cookie'
app.secret_key = 'F130700457'

TOKEN_INFO = 'token_info'
PLAYLIST_NAME = {'EDM','J-pop','K-pop','English','華語歌'}

@app.route('/')
def login():
    auth_url = create_spotify_oauth().get_authorize_url()
    return redirect(auth_url)

@app.route('/redirect')
def redirect_page():
    session.clear()
    code = request.args.get('code')
    token_info = create_spotify_oauth().get_access_token(code)
    session[TOKEN_INFO] = token_info
    return redirect(url_for('save_discover_weekly', external = True))

@app.route('/saveDiscoverWeekly')
def save_discover_weekly():
    try:
        token_info = get_token()
    except:
        print("User not logged in")
        return redirect('/')
    
    #return('OAUTH SUCCESSFUL')
    sp = spotipy.Spotify(auth = token_info['access_token'])
    user_id = sp.current_user()['id']

    discover_weekly_playlist_id = None
    saved_weekly_playlist_id = None

    current_playlists = sp.current_user_playlists()['items']
    for playlist in current_playlists:
        print(playlist['name'])
        if playlist['name'] == 'English':
            discover_weekly_playlist_id = playlist['id']
        if playlist['name'] == 'Saved Weekly':
            saved_weekly_playlist_id = playlist['id']

    if not discover_weekly_playlist_id:
        return 'Discover Weekly not found'
    
    if not saved_weekly_playlist_id:
        new_playlist = sp.user_playlist_create(user_id, 'Saved Weekly', True)
        saved_weekly_playlist_id = new_playlist['id']

    #問題在這裡
    discover_weekly_playlist = sp.playlist_items(discover_weekly_playlist_id, offset = 100) #獲取播放清單歌曲數量或是反轉歌單順序?
    song_uris = []
    count = 0
    print(len(discover_weekly_playlist['items']))
    for song in discover_weekly_playlist['items']:
        song_uri = song['track']['uri']
        song_uris.append(song_uri)
        # count += 1
        # if count > 2:
        #     break
    sp.user_playlist_add_tracks(user_id, saved_weekly_playlist_id, song_uris, None)
    return('wow')

def get_token():
    token_info = session.get(TOKEN_INFO, None)
    if not token_info:
        redirect(url_for('login', external = False))

    now = int(time.time())

    is_expired = token_info['expires_at'] - now < 60
    if is_expired:
        spotify_oauth = create_spotify_oauth()
        token_info = spotify_oauth.refresh_access_token(token_info['refresh_token'])

    return token_info

def create_spotify_oauth():
    return SpotifyOAuth(client_id = '147fa00e19e3487aa8255e50be975262',
                        client_secret = 'dc0b9e3c427b4e5199163f1af460c265',
                        redirect_uri = url_for('redirect_page', _external = True),
                        scope = 'user-library-read playlist-modify-public playlist-modify-private')
                        #scope需要根據不同需求做改變

app.run(debug=True)