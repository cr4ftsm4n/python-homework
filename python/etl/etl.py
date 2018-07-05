def transform(legacy_data):
    result = {}
    for k, v in legacy_data.items():
        for item in v:
            result[item.lower()] = k

    return result
