from datetime import date


class User:

    date_of_birth: date
    
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def Age(self):
        today = date.today()
        return (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )


def test_if_is_adult(func):
    def wrapper(age):
        
        if age >= 18:
                  print("THE PERSON ADULT")
        else:
            raise ValueError("THE PERSON IN TOO YOUNG, AGE :{i} ")
        return func (age)             
    return wrapper

@test_if_is_adult
def just_for_adults(age):
     print(f'PERMITTED AGE {age}')




my_user = User(date(10, 1, 1))
age = my_user.Age
just_for_adults(age)




