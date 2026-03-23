import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PartA import Artist, Song, Album, Playlist

class TestWebFramework(unittest.TestCase):

    def test01_artist_type(self):
        self.assertIsInstance(Artist("Taylor Swift", "1989", "USA"), Artist)

    def test02_song_type(self):
        self.assertIsInstance(Song("Style", "Taylor Swift", 1989), Song)

    def test03_album_type(self):
        self.assertIsInstance(Album("1989", "Taylor Swift", 1989), Album)

    def test04_playlist_type(self):
        self.assertIsInstance(Playlist("Eras"), Playlist)

    def test05_artist_not_song(self):
        self.assertNotIsInstance(Artist("Taylor Swift", "1989", "USA"), Song)

    def test06_song_not_album(self):
        self.assertNotIsInstance(Song("Style", "Taylor Swift", 1989), Album)

    def test07_album_not_playlist(self):
        self.assertNotIsInstance(Album("1989", "Taylor Swift", 1989), Playlist)

    def test08_playlist_not_artist(self):
        self.assertNotIsInstance(Playlist("Eras"), Artist)

    def test09_identity_check(self):
        s1 = Song("Style", "Taylor Swift", 1989)
        s2 = s1
        self.assertIs(s1, s2)

    def test10_non_identity_check(self):
        s1 = Song("Style", "Taylor Swift", 1989)
        s2 = Song("Style", "Taylor Swift", 1989)
        self.assertIsNot(s1, s2)
        
    def test11_album_song_logic(self):
        album = Album("1989", "Taylor Swift", 1989)
        album.add_song("Blank Space", 1989)
        self.assertEqual(len(album.songs), 1)

    def test12_artist_song_logic(self):
        artist = Artist("Taylor Swift", "1989", "USA")
        song = Song("Shake It Off", "Taylor Swift", 1984)
        artist.add_song(song)
        self.assertIn(song, artist.songs)

    def test13_artist_album_logic(self):
        artist = Artist("Taylor Swift", "1989", "USA")
        album = Album("Red", "Taylor Swift", 2012)
        artist.add_album(album)
        self.assertIn(album, artist.albums)

    def test14_playlist_song_logic(self):
        playlist = Playlist("Test")
        song = Song("Bad Blood", "Taylor Swift", 2014)
        playlist.add_song(song)
        self.assertEqual(len(playlist.songs), 1)

    def test15_shuffle_execution(self):
        p = Playlist("Random Mix")
        p.add_song(Song("Style", "Taylor Swift", 1989))
        p.shuffle_playlist() 
        self.assertTrue(True)

    def test16_sort_asc_execution(self):
        p = Playlist("Ordered Mix")
        p.add_song(Song("Style", "Taylor Swift", 1989))
        p.sort_playlist(order='ASC') 
        self.assertTrue(True)

    def test17_sort_des_execution(self):
        p = Playlist("Reverse Mix")
        p.add_song(Song("Style", "Taylor Swift", 1989))
        p.sort_playlist(order='DES') 
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main(verbosity=2)