from random import choice, randint
def us_states():
    state_info = {}
    combiner = zip(state, capital)
    state_info = dict(combiner)
    for key in state_info.key():
        x = input(f"What is the capital of {key}")
        if x == state_info[key]:
            print("Correct!")

print("Example")









