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









