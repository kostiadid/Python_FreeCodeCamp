def verify_card_number(value):
    clean = []
    for ch in value:
        if ch != " " and ch != "-":
            clean.append(ch)

    num_list = []
    summary = 0
    for j in clean:
        num_list.append(int(j))
    for i in range(len(num_list)-1,-1,-1):
        if (len(num_list) -1 -i) % 2 == 1:
            num_list[i] = num_list[i] * 2
            if num_list[i] > 9:
                num_list[i]-=9
        summary+=num_list[i]
    if summary % 10 == 0:
        print("VALID!")
        return "VALID!"
    else:
        print("INVALID!")
        return "INVALID!"

verify_card_number('453914889')
