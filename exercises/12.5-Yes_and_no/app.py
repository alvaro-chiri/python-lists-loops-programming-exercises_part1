theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:
def wikiwoko(x):
    if x == 1:
        return 'wiki'
    else:
        return 'woko'
    
new_list = list(map(wikiwoko, theBools))

print(new_list)


