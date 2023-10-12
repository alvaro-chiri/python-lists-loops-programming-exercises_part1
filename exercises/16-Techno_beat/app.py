def lyrics_generator(arr):
    count = 0
    lyrics = ''

    for i in range(len(arr)):
        if arr[i] == 0:
            lyrics += 'Boom '
            count = 0
        if arr[i] == 1:
            if count == 2:
                lyrics += "Drop the base "
                lyrics += "!!!Break the base!!! "
                count = 0
            else:
                lyrics += "Drop the base "
                count += 1
    
    return lyrics

# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))