from faker import Faker

fake = Faker(locale='en_CA')

aos = 'home_page'
aos_url = 'Advantage Online Shopping'
aos_home_page_url = 'https://advantageonlineshopping.com/#/'
aos_home_page_title = '\xa0Advantage Shopping'

# new_user
f_name = fake.first_name()
l_name = fake.last_name()
username = f'{(f_name + l_name[0:1]).lower()}'
email = f'{username}@gm.ca'
phone = fake.phone_number()
city = fake.city()
country = fake.current_country()
address = fake.street_address()
province = fake.province_abbr()
postal_code = fake.postalcode()
password = fake.password(length=10, special_chars=True, upper_case=True, digits=True)

account_dict = {'usernameRegisterPage': username, 'emailRegisterPage': email, 'passwordRegisterPage': password,
                'confirm_passwordRegisterPage': password}

personal_dict = {'first_nameRegisterPage': f_name, 'last_nameRegisterPage': l_name,
                 'phone_numberRegisterPage': phone}
address_dict = {'cityRegisterPage': city, 'addressRegisterPage': address,
                'state_/_province_/_regionRegisterPage': province, 'postal_codeRegisterPage': postal_code}


