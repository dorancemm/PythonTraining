albums = [
    {"album_name": "Imagine", "artist": "John Lennon",
     "songs" : [("Imagine", 181), ("Crippled Inside", 231),("It's So Hard", 122)],
     "stock":3},
    {"album_name": "Abbey Road", "artist": "The Beatles",
     "songs" : [("Come Together", 260), ("Something", 182),("octupus's Garden", 167)],
     "stock":5}
]

def search_album(albums, album_name=None, artist=None):
    results = []
    for album in albums:
        if album_name and album["album_name"] == album_name:
            results.append(album)
        if artist and album["artist"] == artist:
            results.append(album)
    return results

def search_song(albums, song_name):
    results = []
    for album in albums:
        for song in album["songs"]:
            if song[0] == song_name:
                results.append((song_name, album["album_name"], album["artist"]))
    return results

def buy_albums(albums, album_name):
    for album in albums:
        if album["album_name"] == album_name and album["stock"] > 0:
            album["stock"] -= 1
            print (f"You bought the album {album_name}. Updated Stock: {album['stock']}.")
            return
    print(f"The album {album['album_name']} is not available.")

def bubble_sort_albums(albums):
    n = len(albums)
    for i in range(n):
        for j in range(0, n-i-1):
            if albums[j]["album_name"] > albums[j+1]["album_name"]:
                albums[j], albums[j+1] = albums[j+1], albums[j]

def search_album_name_partial(albums, album_name_partial, index=0):
    if index == len(albums):
        return None
    if album_name_partial in albums[index]["album_name"]:
        return albums[index]
    return search_album_name_partial(albums, album_name_partial, index+1)


# Call Functions
print ("Search album 'Imagine' \n")
print (search_album(albums, album_name="Imagine"))
print ("Search song 'Come Together' \n")
print (search_song(albums, "Come Together"))
print ("Buy album 'Imagine' \n")
buy_albums(albums, album_name="Imagine")
print ("Sort albums \n")
print ("Unordered: ", albums, "\n")
bubble_sort_albums(albums)
print ("Ordered: ", albums, "\n")
print ("Search album (partial name) 'Road' \n")
print (search_album_name_partial(albums, album_name_partial="Road"))


















