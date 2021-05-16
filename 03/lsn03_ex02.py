def user_data(first_name, second_name, year_of_birth, city_address, email, phone_number):
    print(f"first name - {first_name}; second name - {second_name}; year of birth - {year_of_birth}; city address - {city_address}; email - {email}; phone number - {phone_number}")


user_data(first_name = input('enter the first name- '),
          second_name = input('enter the second name- '),
          year_of_birth = input('enter the year of birth- '),
          city_address = input('enter the city address- '),
          email = input('enter the email- '),
          phone_number = input('enter the phone number- '))
