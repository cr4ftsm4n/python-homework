def largest_product(series, size):
    if size ==0:
        return 0
    elif series == "" or size < 0:
        raise ValueError("error")
        
    if size > len(series):
        raise ValueError("error")
        
    seriesu = u"" + series
    if not seriesu.isnumeric():
        raise ValueError("error")
             
    previous=0
    i=0
    t=1
    while i !=len(series)-size+1:
        for num in series[i:i+size]:
            no=int(num)
            t=no*t

        if  t>previous:
            previous = t
        i=i+1
        t=1
    return previous 
