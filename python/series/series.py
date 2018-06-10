def slices(series, length):
    serieslist = []
    i = 0
    if length > len(series) or length < 1:
        raise(ValueError("error"))        
    else:
        for x in range(len(series)-length+1):
            serieslist.append(map(int, list(series[x:x+length])))
            
    return serieslist
