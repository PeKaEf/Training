class Film:
    _list_f = []
    def __init__(self, title, year, genre):
        self.list_f_s = []
        self.list_f_s.append(Film)
        self.title=title
        self.year=year
        self.genre=genre
        self.init_numb_playing = 0

    def play(self,number=1):
        self.init_numb_playing +=number
    
    def __str__(self):
        return f'{self.title} ({self.year})'

class Series(Film):
    _list_s = []
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.list_f_s.append(Series)
        self.episode = episode
        self.season = season
        self.init_play_number = 0
        print(self.list_f_s)
    
    def play_s(self, numb=1):
        self.init_play_number +=numb
    
    def __str__(self):
        return f'{self.title}, S{self.season}E{self.episode}'
    

Omen = Film("Omen","1976","horror")
Hateful_8 = Film("The Hateful Eight","2015","western")
Indiana = Film("Indiana Jones and the Dial of Destiny","2023","adventure")

Office = Series("01","06","The Office", "2005","comedy")
Stranger_T = Series("04","03","Stranger Things","2016","sci-fi")
Squid_G = Series("01","01","Squid Games","2021","thriller")

film_list = []

def get_movies():
    for f in films_series:
        if isinstance(f, Film):
            film_list.append(f)

print(film_list)


