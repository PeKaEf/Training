import random

class Film:
    list_f = []
    def __init__(self, title, year, genre, numb_playing):
        self.list_f.append(self)
        self.title=title
        self.year=year
        self.genre=genre
        self.numb_playing=numb_playing

    def play(self,number=1):
        self.init_numb_playing +=number
    
    def __str__(self):
        return f'{self.title} ({self.year})'
    

class Series(Film):
    def __init__(self, episode, season, title, year, genre, numb_playing):
        Film.__init__(self, title, year, genre, numb_playing)
        self.list_f.append(self)
        self.episode = episode
        self.season = season
        self.title=title
        self.year=year
        self.genre=genre
        self.numb_playing=numb_playing

    def play_s(self, numb=1):
        self.numb_playing +=numb
    
    def __str__(self):
        return f'{self.title}, S{self.season}E{self.episode}'

Omen = Film("Omen","1976","horror","0")
Hateful_8 = Film("The Hateful Eight","2015","western","0")
Indiana = Film("Indiana Jones and the Dial of Destiny","2023","adventure","0")

Office = Series("01","06","The Office", "2005","comedy","0")
Stranger_T = Series("04","03","Stranger Things","2016","sci-fi","0")
Squid_G = Series("01","01","Squid Games","2021","thriller","0")

print(Omen.numb_playing)

film_series = [Omen, Hateful_8, Indiana, Office, Stranger_T, Squid_G]

for f in film_series:
    print(f)

film_list = []
series_list = []

def get_movies():
    for f in film_series:
        if isinstance(f, Film):
            film_list.append(f)
            list_sort = sorted(film_list, key=lambda Film: Film.title)
        else:
            pass
    return print(list_sort)

def get_series():
    for f in film_series:
        if isinstance(f, Series):
            series_list.append(f)
            list_sorted = sorted(series_list, key=lambda Series: Series.title)
        else:
            pass
    return print(list_sorted)

def search(phrase):
    for f in film_series:
        if f == phrase:
            found = print(f)
        else:
            pass
    return found

def generate_views():
    for i in range (1,11):
        randIndex = random.randrange(len(Film.list_f))
        randFilmSeries = Film.list_f[randIndex]
        randViews = random.randrange(1,101)
    return print(Film.title, Film.numb_playing)

def top_titles(content_type):
    if content_type == Film:
        for films in Film.list_f:
            return max(Film.list_f, key=lambda Film: Film.numb_playing)
    elif content_type == Series:
        for films in Film.list_f:
            return max(Series.list_f, key=lambda Series: Series.numb_playing)