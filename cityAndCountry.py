def city_country(city_name, country_name):
    full_city_country = f"{city_name}, {country_name}"
    #print(full_city_country)
    return full_city_country


while True:
    print("\nPlease tell me the city name of you coming from: ")
    print("\n(Enter 'q' at any time to quit.)")
    city_name = input("Which city are you from: ")
    if city_name == 'q':
        break
    country_name = input("Which country does it belong: ")
    if country_name == 'q':
        break

    full_address = city_country(city_name, country_name)
    print(f"\n“{full_address}” " )


