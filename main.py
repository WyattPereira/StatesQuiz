# US States Quiz
import numpy


def provinces():
    score_2 = 0
    while True:
        dict_prov_list = list(province_info.items())
        numpy.random.shuffle(dict_prov_list)
        new_prov_dict = dict(dict_prov_list)
        for key,value in new_prov_dict.items():
            y = input(f"What is the capital of {key}?: ")
            if y.title() == province_info[key]:
                print("Correct!")
                score_2 += 1
            else:
                print("Wrong answer!")
                print("\nGAME OVER!")
                print(f"Your Score Was: {score_2}!")
                exit()


def us_states():
    score = 0
    while True:
        dict_list = list(state_info.items())
        numpy.random.shuffle(dict_list)
        new_dict = dict(dict_list)
        for key,value in new_dict.items():
            x = input(f"What is the capital of {key}?: ")
            if x.title() == state_info[key]:
                print("Correct!")
                score += 1
            else:
                print("Wrong answer!")
                print("\nGAME OVER!")
                print(f"Your Score Was: {score}!")
                exit()


state_info = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
}

province_info = {
    'Quebec': 'Quebec City',
    'Ontario': 'Toronto',
    'Newfoundland and Labrador': "St.John's",
    'P.E.I.': 'Charlottetown',
    'New Brunswick': 'Fredericton',
    'Nova Scotia': 'Halifax',
    'Manitoba': 'Winnipeg',
    'Saskatchewan': 'Regina',
    'Alberta': 'Edmonton',
    'British Colombia': 'Victoria',
    'Yukon': 'Yellowknife',
    'N.W.T.': 'White Horse',
    'Nunavut': 'Iqaluit'
}


# Intro
print("Welcome To The U.S. States and Canadian Provinces Quiz!\n")
print("You will be tested on your knowledge of states, provinces, and their capital city")
selection = input("Would you like to study state capitals or provincial capitals? [S|P] : ")
# Selection Menu
if selection.title() in "S":
    print("\nLet's Begin!\n")
    us_states()
elif selection.title() in "P":
    print("\nLet's Begin!\n")
    provinces()
else:
    print("Error: Invalid Entry.\nPlease try again")








