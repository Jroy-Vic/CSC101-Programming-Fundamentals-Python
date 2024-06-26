import data

# Write your functions for each part in the space below.

# Part 1
# Purpose: this function takes two data.Point values and returns
#          a data.Rectangle value based on those inputted points without
#          any previous assumptions about the points' locations.
# Input: data.Point, data.Point
# Output: data.Rectangle
# Example Input: data.Point(2,2), data.Point(10,10)
# Example Output: data.Rectangle(data.Point(2,10), data.Point(10,2))

def create_rectangle(p1: data.Point, p2: data.Point) -> data.Rectangle:
    pnt_hold = 0
    if p1.x <= p2.x:
        p3_x = p1.x
        p4_x = p2.x
        top_left = data.Point(p3_x, pnt_hold)
        bottom_right = data.Point(p4_x, pnt_hold)
    else:
        p3_x = p2.x
        p4_x = p1.x
        top_left = data.Point(p3_x, pnt_hold)
        bottom_right = data.Point(p4_x, pnt_hold)
    if p1.y >= p2.y:
        p3_y = p1.y
        p4_y = p2.y
        top_left = data.Point(p3_x, p3_y)
        bottom_right = data.Point(p4_x, p4_y)
    else:
        p3_y = p2.y
        p4_y = p1.y
        top_left = data.Point(p3_x, p3_y)
        bottom_right = data.Point(p4_x, p4_y)
    rectangle = data.Rectangle(top_left, bottom_right)
    return rectangle

# Part 2
# Purpose: this function takes in two data.Duration values and
#          returns a boolean value; it returns True if the first
#          data.Duration value is shorter than the second, returns False otherwise.
# Input: data.Duration, data.Duration
# Output: bool
# Example Input: data.Duration(5,25), data.Duration(8,45)
# Example Output: True

def shorter_duration_than(dur1: data.Duration, dur2: data.Duration) -> bool:
    return dur1.minutes < dur2.minutes or (dur1.minutes == dur2.minutes and dur1.seconds < dur2.seconds)

# Part 3
# Purpose: this function takes in two different types of inputs,
#          the first is a list of data.Song values and the second
#          is a data.Duration value; it returns a list of all data.Song values
#          in the input list with a shorter duration than the inputted value.
# Input: list[data.Song], data.Duration
# Output: list[data.Song]
# Example Input: [data.Song("grentperez", "About Love", data.Duration(4,18)), data.Song("Luna Li", "2516", data.Duration(1,8)), data.Song("keshi", "SOMEBODY", data.Duration(2,44))], data.Duration(3,0)
# Example Output: [data.Song("Luna Li", "2516", data.Duration(1,8)), data.Song("keshi", "SOMEBODY", data.Duration(2,44))]

def songs_shorter_than(list_in: list[data.Song], dur: data.Duration) -> list[data.Song]:
    list_out = []
    for songs in list_in:
        if songs.duration.minutes < dur.minutes:
            list_out.append(songs)
        elif songs.duration.minutes == dur.minutes:
            if songs.duration.seconds < dur.seconds:
                list_out.append(songs)
    return list_out

# Part 4
# Purpose: this function takes two inputs, the first is a list of data.Song values and the
#          second is a list of int values representing which song is being added to the playlist;
#          returns the total data.Duration value of all the data.Song values included in the playlist.
# Input: list[data.Song], list[int]
# Output: data.Duration
# Example Input: [data.Song("grentperez", "About Love", data.Duration(4,18)), data.Song("Luna Li", "2516", data.Duration(1,8)), data.Song("keshi", "SOMEBODY", data.Duration(2,44))], [0, 1, 2, 0, 1, 2]
# Example Output: data.Duration(16, 20)

def running_time(list_songs: list[data.Song], list_int: list[int]) -> data.Duration:
    minutes = 0
    seconds = 0
    if len(list_int) == 0:
        return None
    else:
        for n in list_int:
            if n <= (len(list_songs) - 1) and n >= 0:
                selected_song = list_songs[n]
                minutes = minutes + selected_song.duration.minutes
                seconds = seconds + selected_song.duration.seconds
                if seconds >= 60:
                    add_minutes = seconds // 60
                    excess_seconds = seconds % 60
                    seconds = excess_seconds
                    minutes = minutes + add_minutes
                total_time = data.Duration(minutes, seconds)
        return total_time

# Part 5
# Purpose: this function takes two inputs, the first being a list nested lists of str values
#          and the second being a list of str values; returns a boolean value;
#          returns True if the second input is a valid connection from the given routes
#          in the first inputted list.
# Input: list[list[str], list[str]
# Output: bool
# Example Input: [
#                ['san luis obispo', 'santa margarita'],
#                ['san luis obispo', 'pismo beach'],
#                ['atascadero', 'santa margarita'],
#                ['atascadero', 'creston']
#                ],
#                ['san luis obispo', 'santa margarita', 'atascadero']
# Example Output: True

def validate_route(list_connections: list[list[str]], list_route: list[str]) -> bool:
    if list_route == []:
        return True
    elif len(list_route) == 1:
        for idx in range(len(list_connections)):
            if list_route[0] in list_connections[idx]:
                return True
    else:
        for idx in range((len(list_route))):
            if idx < (len(list_route) - 1):
                list_1 = []
                list_1.append(list_route[idx])
                list_1.append((list_route[idx + 1]))
                list_swap = []
                list_swap.append(list_route[idx + 1])
                list_swap.append(list_route[idx])
            if list_1 not in list_connections and list_swap not in list_connections:
                return False
        return True


# Part 6
# Purpose: this function takes a list of int values and returns the index
# at which the longest contiguous repetition begins, or None if no repetition occurs.
# Input: list[int]
# Output: int
# Example Input: [1, 1, 2, 2, 1, 1, 1, 3]
# Example Output: 4

def longest_repetition(list_in: list[int]) -> int:
    count = 0
    final_count = 0
    idx_rep = 0

    for idx in range(len(list_in)):
        if idx == 0:
            count = 1
        elif idx == len(list_in) - 1:
            if list_in[len(list_in) - 1] == list_in[idx - 1]:
                if (count + 1) >= final_count:
                    idx_rep = idx - count
        elif (list_in[idx] == list_in[idx + 1]) and (list_in[idx] == list_in[idx - 1]):
            count = count + 1
        elif (list_in[idx] != list_in[idx + 1]) and (list_in[idx] == list_in[idx - 1]):
            if (count + 1) >= final_count:
                idx_rep = idx - count
            final_count = count + 1
            count = 0
        elif (list_in[idx] == list_in[idx + 1]) and (list_in[idx] != list_in[idx - 1]):
            count = 1
        elif list_in[len(list_in) - 1] == list_in[idx - 1]:
            if (count + 1) >= final_count:
                idx_rep = idx - count

    if final_count == 0:
        return None
    return idx_rep
