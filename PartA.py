import random

class Song:
    def __init__(self, title, artist_name, year):
        self.title       = title
        self.artist_name = artist_name
        self.year        = year

    def display_info(self):
        print(f"  Title   : {self.title}")
        print(f"  Artist  : {self.artist_name}")
        print(f"  Year    : {self.year}")

class Album:
    def __init__(self, title, artist_name, year):
        self.title       = title
        self.artist_name = artist_name
        self.year        = year
        self.songs       = []

    def display_info(self):
        song_names = [s.title for s in self.songs] if self.songs else ["None"]
        print(f"  Album   : {self.title}")
        print(f"  Artist  : {self.artist_name}")
        print(f"  Year    : {self.year}")
        print(f"  Tracks  : {song_names}")

    def add_song(self, title, year):
        new_song = Song(title, self.artist_name, year)
        self.songs.append(new_song)
        return new_song

class Artist:
    def __init__(self, name, dob, country):
        self.name    = name
        self.dob     = dob
        self.country = country
        self.albums  = []
        self.songs   = []

    def display_info(self):
        album_names = [a.title for a in self.albums] if self.albums else ["None"]
        song_names  = [s.title for s in self.songs]  if self.songs  else ["None"]
        print(f"  Name    : {self.name}")
        print(f"  DOB     : {self.dob}")
        print(f"  Country : {self.country}")
        print(f"  Albums  : {album_names}")
        print(f"  Songs   : {song_names}")

    def add_album(self, album):
        self.albums.append(album)

    def add_song(self, song):
        self.songs.append(song)

class Playlist:
    def __init__(self, title):
        self.title = title
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def print_all_song(self):
        print(f"\n  [{self.title}]")
        if not self.songs:
            print("  (empty playlist)")
            return
        for index, track in enumerate(self.songs, start=1):
            print(f"  {index:>2}. {track.title} — {track.artist_name} ({track.year})")

    def sort_playlist(self, order='ASC'):
        reverse = order != 'ASC'
        self.songs.sort(key=lambda track: track.title, reverse=reverse)
        print(f"Playlist '{self.title}' sorted in {'ASCENDING' if order=='ASC' else 'DESCENDING'} order")

    def shuffle_playlist(self):
        random.shuffle(self.songs)
        print(f"Playlist '{self.title}' has been shuffled")

def section(heading):
    print("\n" + "─" * 50)
    print(f"  {heading}")
    print("─" * 50)

if __name__ == '__main__':
    section("Artist Info")
    ts = Artist("Taylor Swift", "13-12-1989", "USA")
    ts.display_info()

    section("Album 1989")
    album_1989 = Album("1989", ts.name, 1989)
    album_1989.display_info()

    section("songs for album 1989")
    album_1989.add_song("Welcome To New York", 1989)
    album_1989.add_song("Blank Space", 1989)
    album_1989.add_song("Style", 1989)
    album_1989.add_song("Out Of The Woods", 1989)
    album_1989.add_song("Shake It Off", 1989)
    album_1989.add_song("Bad Blood", 1989)
    album_1989.add_song("Wildest Dreams", 1989)
    album_1989.add_song("New Romantics", 1989)
    album_1989.display_info()

    section("Album 2: Fearless")
    album_fearless = Album("Fearless", ts.name, 2008)
    album_fearless.add_song("Love Story", 2008)
    album_fearless.add_song("You Belong With Me", 2008)
    album_fearless.add_song("Fifteen", 2008)
    album_fearless.display_info()

    section("Album Update")
    ts.add_album(album_1989)
    ts.add_album(album_fearless)

    for track in album_1989.songs:
        ts.add_song(track)

    ts.display_info()

    section("Create playlist")
    my_mix = Playlist("1989 Essentials")

    section("Add songs To Playlist")
    for track in album_1989.songs:
        my_mix.add_song(track)

    my_mix.print_all_song()

    section("ASC Order")
    my_mix.sort_playlist(order='ASC')
    my_mix.print_all_song()

    section("Sort Playlist")
    my_mix.sort_playlist(order='DES')
    my_mix.print_all_song()

    section("Shuffle Playlist")
    my_mix.shuffle_playlist()
    my_mix.print_all_song()

    section("Display song info")
    album_1989.songs[0].display_info()