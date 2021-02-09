LEGAL_DRINKING_AGE = 18

def enter_night_club(age):
    if age > LEGAL_DRINKING_AGE:
        print("Allowed to enter.")
    else:
        print("Enterance of minors is denited.")


age = 17.9
enter_night_club(age)
