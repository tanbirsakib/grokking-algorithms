houses = ["Sakib's House", "Tuhin's House", "Younus's house", "Baizid's house"]

def deliver_recursively(houses):
    if len(houses) == 1:
        print('deliver present to ', houses[0])

    #distributing to sub task
    else:
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]
        deliver_recursively(first_half)
        deliver_recursively(second_half)

deliver_recursively(houses)