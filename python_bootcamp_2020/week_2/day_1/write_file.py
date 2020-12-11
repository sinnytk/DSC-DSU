from time import sleep

with open("test.txt") as song_file:
    print(song_file.closed)
    song_lyrics = song_file.read()
    # for line in song_lyrics.split("\n"):
    #     print(line)
    #     sleep(1)

print(song_file.closed)