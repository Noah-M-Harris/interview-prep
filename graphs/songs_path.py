'''
Our local radio station is running a show where the songs are ordered in a very specific way.  The last word of the title of one song must match the first word of the title of the next song - for example, "Silent Running" could be followed by "Running to Stand Still".  No song may be played more than once.

Given a list of songs and a starting song, find the longest chain of songs that begins with that song, and the last word of each song title matches the first word of the next one.  Write a function that returns the longest such chain. If multiple equivalent chains exist, return any of them.

Example:
songs1 = [
    "Down By the River",
    "River of Dreams",
    "Take me to the River",
    "Dreams",
    "Blues Hand Me Down",
    "Forever Young",
    "American Dreams",
    "All My Love",
    "Cantaloop",
    "Take it All",
    "Love is Forever",
    "Young American",
    "Every Breath You Take",
]
song1_1 = "Every Breath You Take"
chaining(songs1, song1_1) => ['Every Breath You Take', 'Take it All', 'All My Love', 'Love is Forever', 'Forever Young', 'Young American', 'American Dreams', 'Dreams']

Additional Input:
song1_2 = "Dreams"
song1_3 = "Blues Hand Me Down"
song1_4 = "Cantaloop"

songs2 = [
    "Bye Bye Love",
    "Nothing at All",
    "Money for Nothing",
    "Love Me Do",
    "Do You Feel Like We Do",
    "Bye Bye Bye",
    "Do You Believe in Magic",
    "Bye Bye Baby",
    "Baby Ride Easy",
    "Easy Money",
    "All Right Now",
]
song2_1 = "Bye Bye Bye"
song2_2 = "Bye Bye Love"

songs3 = [
    "Love Me Do",
    "Do You Believe In Magic",
    "Magic You Do",
    "Magic Man",
    "Man In The Mirror"
]
song3_1 = "Love Me Do"

All Test Cases:
chaining(songs1, song1_1) => ['Every Breath You Take', 'Take it All', 'All My Love', 'Love is Forever', 'Forever Young', 'Young American', 'American Dreams', 'Dreams']
chaining(songs1, song1_2) => ['Dreams']
chaining(songs1, song1_3) => ['Blues Hand Me Down', 'Down By the River', 'River of Dreams', 'Dreams']
chaining(songs1, song1_4) => ['Cantaloop']
chaining(songs2, song2_1) => ['Bye Bye Bye', 'Bye Bye Baby', 'Baby Ride Easy', 'Easy Money', 'Money for Nothing', 'Nothing at All', 'All Right Now']
chaining(songs2, song2_2) => ['Bye Bye Love', 'Love Me Do', 'Do You Feel Like We Do', 'Do You Believe in Magic']
chaining(songs3, song3_1) => ['Love Me Do', 'Do You Believe in Magic', 'Magic Man', 'Man In The Mirror']

Complexity Variable:
n = number of songs in the input


'''
songs1 = [
    "Down By the River",
    "River of Dreams",
    "Take me to the River",
    "Dreams",
    "Blues Hand Me Down",
    "Forever Young",
    "American Dreams",
    "All My Love",
    "Cantaloop",
    "Take it All",
    "Love is Forever",
    "Young American",
    "Every Breath You Take",
]
song1_1 = "Every Breath You Take"
song1_2 = "Dreams"
song1_3 = "Blues Hand Me Down"
song1_4 = "Cantaloop"

songs2 = [
    "Bye Bye Love",
    "Nothing at All",
    "Money for Nothing",
    "Love Me Do",
    "Do You Feel Like We Do",
    "Bye Bye Bye",
    "Do You Believe in Magic",
    "Bye Bye Baby",
    "Baby Ride Easy",
    "Easy Money",
    "All Right Now",
]
song2_1 = "Bye Bye Bye"
song2_2 = "Bye Bye Love"

songs3 = [
    "Love Me Do",
    "Do You Believe In Magic",
    "Magic You Do",
    "Magic Man",
    "Man In The Mirror"
]
song3_1 = "Love Me Do"
        
       
from collections import defaultdict
def solution(songs, starting_song):
    # loop over songs, we'll map every ending of a song to any new songs that begin with that word
    graph = defaultdict(list)

    for song in songs:
        words  = song.split(" ")
        first = words[0]
        graph[first].append(song)
    

    # the song is the beginning of a path
    length = [float("-inf")]
    visited = set()
    result = [1]
    def dfs(song, path):
        '''
        if song in visited:
            if length[-1] < len(path):
                result[-1] = path[:]
                length[-1] = len(path)
            return
        '''
        
        visited.add(song)
        path.append(song)

        if length[-1] < len(path):
            result[-1] = path[:]
            length[-1] = len(path)

        words = song.split(" ")
        last = words[-1]
        for s in graph[last]:
            if s not in visited:
                dfs(s, path)
        
        path.pop()
        visited.remove(song)
        return

    dfs(starting_song, [])
    # print(starting_song)
    return result[-1]

print(solution(songs1, song1_1))
print(solution(songs1, song1_2))
print(solution(songs1, song1_3))
print(solution(songs1, song1_4))
print(solution(songs2, song2_1))
print(solution(songs2, song2_2))
print(solution(songs3, song3_1))
