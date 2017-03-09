import sqlite3
import json
import codecs
import os

cx = sqlite3.connect(os.path.expanduser('~') + "/Library/Containers/com.netease.163music/Data/Documents/storage/sqlite_storage.sqlite3")
cx.row_factory = sqlite3.Row


def getPlaylistNameFromJson(jsonStr):
	playlistDetail = json.loads(jsonStr)
	# return playlistDetail["name"].encode("GBK", 'ignore');
	return playlistDetail["name"].encode("utf-8", 'ignore');

def getMusicNameFromJson(jsonStr):
	musicDetail = json.loads(jsonStr)
	return musicDetail["name"];

def getArtistNameFromJson(jsonStr):
	load = json.loads(jsonStr)
	ret = []
	for artist in load["artists"]:
		ret.append(artist["name"].encode("utf-8", 'ignore'))
	return ret

def getPlaylist():
	cu = cx.cursor()
	cu.execute("select * from web_playlist") 
	playlists = []
	for item in cu.fetchall():
		playlist = (item["pid"], getPlaylistNameFromJson(item["playlist"]))
		playlists.append(playlist)
	return playlists

def getPlayListMusic(pid):
	cu = cx.cursor()
	cu.execute("select * from web_playlist_track where pid=?",[pid]) 
	musics=[]
	for item in cu.fetchall():
		musics.append(item["tid"]);
	return musics

def getMusicDetail(tid):
	cu = cx.cursor()
	cu.execute("select * from web_track where tid=?",[tid]) 
	music = cu.fetchone()
	if music is None:
		return None
	# detail = (getMusicNameFromJson(music["detail"]), music["relative_path"])
	musicName = getMusicNameFromJson(music["track"])
	musicArtists = getArtistNameFromJson(music["track"])
	return (musicName, musicArtists)


def main():
	playlists = getPlaylist()
	for item in playlists:
		playlistID = item[0]
		playlistName = item[1]

		output = open(os.getcwd() + "/" + playlistName + ".csv", 'w')

		musicIds = getPlayListMusic(playlistID)
		for tid in musicIds:
			if tid is not None:
				musicName, musicArtists = getMusicDetail(tid)
				if musicName is not None:
					output.write(musicName.encode("utf-8", 'ignore'))
					for artist in musicArtists:
						output.write(", " + artist)
					output.write("\n")
	cx.close()

if __name__ == '__main__':
	main()


# References:
# 1. https://github.com/vileer/NeteaseCloudMusicPlaylistCreator
# 2. Online sqlite3 viewer: http://inloop.github.io/sqlite-viewer/
# 3. Online JSON viewer: http://json.parser.online.fr/
# 4. http://stackoverflow.com/questions/9942594/unicodeencodeerror-ascii-codec-cant-encode-character-u-xa0-in-position-20