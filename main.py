def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order
             in which they were chosen."""
    new_playlist = []
    space_remaining = max_size
    for song in songs[0]:
        if song[2] > space_remaining:
            continue
        else:
            if song not in new_playlist:
                new_playlist.append(song)
                space_remaining -= song[2]

    sorted_songs = sorted(songs, key=lambda song: song[2])

    for song in range(len(sorted_songs)):
        listed_song = list(sorted_songs[song])

    for song[2] in sorted_songs:
        if song[2] > space_remaining:
            continue
        else:
            if song not in new_playlist:
                new_playlist.append(song)
                space_remaining -= song[2]
    print(space_remaining)
    return new_playlist


songs = [('Roar', 4.4, 4.0), ('Sail', 3.5, 7.7), ('Timber', 5.1, 6.9), ('Wannabe', 2.7, 1.2)]
max_size = 12.2

