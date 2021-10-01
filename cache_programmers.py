def solution(cacheSize, cities):#LRU
    time = 0
    cache = []
    cities = [city.lower() for city in cities]
    if cacheSize != 0:
        for city in cities:
            if city in cache:
                cache.pop(cache.index(city))
                cache.append(city)
                time += 1
            else:
                if len(cache) < cacheSize:
                    cache.append(city)
                    time += 5
                else:
                    cache.pop(0)
                    cache.append(city)
                    time += 5
    else: time += len(cities) * 5
    return time

