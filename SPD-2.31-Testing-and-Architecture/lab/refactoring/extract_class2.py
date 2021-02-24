class Actors:
    def __init__(self, first_names, last_names, birth_year, movies):
        self.first_names = ['Elizabeth', 'Jim']
        self.last_names = ['Debicki', 'Carrey']
        self.birth_year = [1990, 1962]
        self.movies = [['Tenet', 'Vita & Virginia', 'Guardians of the Galaxy', 'The Great Gatsby'],\
                        ['Ace Ventura', 'The Mask', 'Dumb and Dumber', 'The Truman Show', 'Yes Man']]
        self.emails = ['deb@makeschool.com', 'jim@makeschool.com']

    def send_hiring_email(self, emails):
        for i, email in enumerate(emails):
            if self.birth_year[i] > 1985:
                print(self.first_names[i], self.last_names[i])
                print('Movies Played: ', end=' ')
                for m in self.movies[i]:
                    print(m, end=', ')
                print()
                print("email sent to: ", email)