# Functionality
- Export play list and song names from [Netease Music](http://music.163.com/) **for Mac users**.
- One **.csv** file per play list, which contains all songs and artist names of that play list.
- The output directory is simply the current working directory.

# Run
- Open your **Terminal**.
- Run `python export-netease-music-playlist.py`.

# Attention
- **Only** for Mac users.
- Windows users please check here: https://github.com/vileer/NeteaseCloudMusicPlaylistCreator
- The location of **sqlite\_storage.sqlite3** might differ on your Mac. So you'll probably need to search for this file and then assign that value to variable **database_path**.

# Testing
- Only tested on **OS X Yosemite 10.10.5**, with **Python 2.7.13** and **Netease Music Version 1.5.1**.

# Acknowledgement
- Many thanks to [vileer](https://github.com/vileer/NeteaseCloudMusicPlaylistCreator)'s project!
- I borrowed a lot from his code and his code actually saved tons of my time while developing this toy project.

# Copyright
- Please feel free to copy and mofidy this code.
