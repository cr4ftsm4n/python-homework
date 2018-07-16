 def recite(start, take=1):
    song = []
    count  = start
    for i in range(1, take+1):
        if len(song) > 0:
            song.append("")
        if count == 0:
            song.append("No more bottles of beer on the wall, no more bottles of beer.")
            song.append("Go to the store and buy some more, 99 bottles of beer on the wall.")
            count = 99
        elif count == 1:
            song.append("1 bottle of beer on the wall, 1 bottle of beer.")
            song.append("Take it down and pass it around, no more bottles of beer on the wall.")
            count = 0
        elif count == 2:
            song.append("2 bottles of beer on the wall, 2 bottles of beer.")
            song.append("Take one down and pass it around, 1 bottle of beer on the wall.")
            count = 1
        else:
            song.append(str(count)+" bottles of beer on the wall, "+ str(count) + " bottles of beer.")
            song.append("Take one down and pass it around, "+ str(count-1) + " bottles of beer on the wall.")
            count -= 1
    return song
        
