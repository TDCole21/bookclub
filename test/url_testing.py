import urllib3

#####################################################################################################################################################################
#########################################################################     TEST HOME     #########################################################################
#####################################################################################################################################################################


def test_homepage():                                                        #tests if page exists(homepage)
    http=urllib3.PoolManager()
    r = http.request('GET', 'http://35.242.157.109:5000/home')
    assert 200 == r.status #200 is successful connection

def test_indexpage():                                                        #tests if page exists(index)
    http=urllib3.PoolManager()
    r = http.request('GET', 'http://35.242.157.109:5000/index')
    assert 200 == r.status #200 is successful connection

def test_deafult():                                                        #tests if page exists(default)
    http=urllib3.PoolManager()
    r = http.request('GET', 'http://35.242.157.109:5000/')
    assert 200 == r.status #200 is successful connection

def test_home_search():                                                        #tests if page exists(search on homepage)
    http=urllib3.PoolManager()
    r = http.request('GET', 'http://35.242.157.109:5000/home/search')
    assert 500 == r.status #500 because variables won't be assigned

def test_home_link():                                                        #tests if page exists
    http=urllib3.PoolManager()
    r = http.request('GET', 'http://35.242.157.109:5000/home/link')
    assert 200 == r.status #200 is successful connection

def test_home_dissociate():                                                        #tests if page exists(homepage)
    http=urllib3.PoolManager()
    r = http.request('GET', 'http://35.242.157.109:5000/home/dissociate')
    assert 500 == r.status #500 because variables won't be assigned

def test_home_delete_actors_all():                                                        #tests if page exists(homepage)
    http=urllib3.PoolManager()
    r = http.request('GET', 'http://35.242.157.109:5000/home/delete/actors/all')
    assert 500 == r.status #500 because variables won't be assigned

def test_home_delete_films_all():                                                        #tests if page exists(homepage)
    http=urllib3.PoolManager()
    r = http.request('GET', 'http://35.242.157.109:5000/home/delete/films/all')
    assert 500 == r.status #500 because variables won't be assigned

def test_home_create_many():                                                        #tests if page exists(homepage)
    http=urllib3.PoolManager()
    r = http.request('GET', 'http://35.242.157.109:5000/home/create/many')
    assert 200 == r.status #200 is successful connection

#####################################################################################################################################################################
########################################################################     TEST ACTORS     ########################################################################
#####################################################################################################################################################################

def test_actors():                                                      #tests if page exists(Activities)
    http=urllib3.PoolManager()
    r=http.request('GET', 'http://35.242.157.109:5000/actors')
    assert 200  == r.status

def test_actors_create():                                                      #tests if page exists(Activities)
    http=urllib3.PoolManager()
    r=http.request('GET', 'http://35.242.157.109:5000/actors/create')
    assert 200  == r.status

def test_actors_delete():                                                      #tests if page exists(Activities)
    http=urllib3.PoolManager()
    r=http.request('GET', 'http://35.242.157.109:5000/actors/delete')
    assert 200  == r.status

def test_actors_update():                                                      #tests if page exists(Activities)
    http=urllib3.PoolManager()
    r=http.request('GET', 'http://35.242.157.109:5000/actors/update')
    assert 200  == r.status

####################################################################################################################################################################
########################################################################     TEST FILMS     ########################################################################
####################################################################################################################################################################


def test_films():                                                        #tests if page exists(Locations)
    http=urllib3.PoolManager()
    r=http.request('GET', 'http://35.242.157.109:5000/films')
    assert 200  == r.status

def test_films_create():                                                        #tests if page exists(Locations)
    http=urllib3.PoolManager()
    r=http.request('GET', 'http://35.242.157.109:5000/films/create')
    assert 200  == r.status

def test_films_delete():                                                        #tests if page exists(Locations)
    http=urllib3.PoolManager()
    r=http.request('GET', 'http://35.242.157.109:5000/films/delete')
    assert 200  == r.status

def test_films_update():                                                        #tests if page exists(Locations)
    http=urllib3.PoolManager()
    r=http.request('GET', 'http://35.242.157.109:5000/films/update')
    assert 200  == r.status

#####################################################################################################################################################################
#########################################################################     TEST MISC     #########################################################################
#####################################################################################################################################################################


def test_nonpage():                                                         #tests if page doesn't exist
    http=urllib3.PoolManager()
    r=http.request('GET', 'http://35.242.157.109:5000/aboutus')
    assert 404  == r.status

    