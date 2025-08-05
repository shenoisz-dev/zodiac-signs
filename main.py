import re

ZODIACS = {
    120: {'zodiac': 'Capricorn', 'from': '22-12 to 20-01', 'planet': 'Saturn', 'god': 'Chronos'},
    219: {'zodiac': 'Aquarius', 'from': '21-02 to 19-02', 'planet': 'Uranus', 'god': 'Ouranus'},
    320: {'zodiac': 'Pisces', 'from': '20-02 to 20-03', 'planet': 'Neptune', 'god': 'Poseidon'},
    420: {'zodiac': 'Aries', 'from': '21-03 to 20-04', 'planet': 'Mars', 'god': 'Ares'},
    520: {'zodiac': 'Taurus', 'from': '21-04 to 20-05', 'planet': 'Venus', 'god': 'Aphrodite'},
    620: {'zodiac': 'Gemini', 'from': '21-05 to 20-06', 'planet': 'Mercury', 'god': 'Hermes'},
    721: {'zodiac': 'Cancer', 'from': '21-06 to 21-07', 'planet': 'Moon', 'god': 'Selene'},
    822: {'zodiac': 'Leo', 'from': '22-07 to 22-08', 'planet': 'Sun', 'god': 'Apollo'},
    922: {'zodiac': 'Virgo', 'from': '23-08 to 22-09', 'planet': 'Mercury', 'god': 'Hermes'},
    1022: {'zodiac': 'Libra', 'from': '23-09 to 22-10', 'planet': 'Venus', 'god': 'Aphrodite'},
    1121: {'zodiac': 'Scorpio', 'from': '23-10 to 21-11', 'planet': 'Mars', 'god': 'Ares'},
    1221: {'zodiac': 'Sagittarius', 'from': '22-11 to 21-12', 'planet': 'Jupiter', 'god': 'Zeus'}
}

class ZodiacSigns():
    error_msg = "Something wrong with the format or length!"

    def validate_date(self, day : int, mounth: int) -> []:
        if (day < 1 or day > 31):
            raise("Give a day greater then 1 and less then 32!")
        if (mounth < 1  or mounth > 12):
            raise("Give a mounth greater then 1 and less then 13!")
        return day, mounth

    def get_formated_date(self, birthday_date) -> []:
        birthday_date = re.sub(r"/", "-", birthday_date)

        if '-' in birthday_date and len(birthday_date) < 3:
            raise(self.error_msg)
        
        birthday_date = birthday_date.split("-")

        if len(birthday_date) > 3:
            raise(self.error_msg)
        
        if len(birthday_date) > 2:
            birthday_date.pop()
        
        day, mounth = int(birthday_date[0]), int(birthday_date[1])
        return self.validate_date(day, mounth)

    def get_zodiac_info(self, day : int, mounth: int) -> dict:
        if day < 10:
            day = "0" + str(day)
        key = str(mounth) + str(day)
        key = int(key)

        if key > 1221:
            key = 120
        
        for zodiac in ZODIACS:
            if key <= zodiac:
                return ZODIACS[zodiac]
    
    def get_zodiac(self, *args, **kwargs) -> dict:
        if 'birthday' in kwargs:
            day, mounth = self.get_formated_date(kwargs['birthday'])
        elif 'day' in kwargs and 'mounth' in kwargs:
            day, mounth = self.validate_date(kwargs['day'], kwargs['mounth'])
        else:
            raise("Pass birthday=str or day=int,mounth=int!")
        return self.get_zodiac_info(day, mounth)

    def input_date(self):
        birthday_date = input("Give your birthday date(only day and mounth): ")
        day, mounth = self.get_formated_date(birthday_date)
        result = self.get_zodiac_info(day, mounth)
        print(result)


zs = ZodiacSigns()
#zs.input_date()
print(zs.get_zodiac(day=31, mounth=3))
