from weather import city_national_free

cities = city_national_free.cities


def parselist(dt, search='', path=[]):
    for v in dt:
        if type(v) is str:
            parsestr(v)
        elif type(v) is dict:
            ret = parsedict(v, search, path)
            if ret is not None:
                return ret
        elif type(v) is list:
            parselist(v, search, path)
        else:
            print(v)
    path.pop()


def parsedict(dt, search='', path=[]):
    if 'list' in dt.keys():
        path.append(dt['name'])
        ret = parselist(dt['list'], search, path)
        if ret is not None:
            return ret
    else:
        city_id = dt.get('city_id','')
        city_name = dt.get('name','')
        city_en = dt.get('en','')
        if search != '' and search.lower() in (city_id,city_name,city_en.lower()):
            return {'city_id':city_id,'name':city_name,'en':city_en}


def parsestr(dt, path=[]):
    print(dt)


def get_en_by_name(name):
    return parsedict(cities, name)

# get_en_by_name('北京')