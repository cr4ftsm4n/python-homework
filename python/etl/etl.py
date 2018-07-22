def transform(legacy_data):
    dictemp = {}
    for key, value in legacy_data.items():
        for i in value:
            dictemp[i.lower()] = key
    
    items = dictemp.keys()
    items.sort()
    
    dic = {}
    for item in items:
        dic[item] = dictemp[item]
    
    return dic
