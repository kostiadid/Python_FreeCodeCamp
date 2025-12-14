full_dot = '●'
empty_dot = '○'

def create_character(name,strength, intelligence, charisma):
    if not isinstance(name, str):
        return 'The character name should be a string'
    if len(name) >= 11:
        return 'The character name is too long'
    for n in  name :
        if n == ' ':
            return 'The character name should not contain spaces'
    stats = [strength,intelligence,charisma]
    part = ''
    full_string  = ''
    for idx, n in enumerate(stats):
            if idx == 0:
                part = '\nSTR '
            elif idx == 1:
                part = '\nINT '
            elif idx == 2:
                part = '\nCHA '
            if not isinstance(n,int):
                return 'All stats should be integers'
            if n < 1:
                return 'All stats should be no less than 1' 
            if n > 4:
                return 'All stats should be no more than 4' 
            for i in range(0, n): 
                part=part+full_dot
            empty = 10 - n
            for i in range(0, empty): 
                part= part+empty_dot
            full_string += part
    sum = strength + intelligence + charisma
    if sum != 7 :
        return 'The character should start with 7 points'
    # print(full_string)
    full_data  = name + full_string
    # print(full_data)
    return  full_data


create_character("Bob",3, 2, 2)