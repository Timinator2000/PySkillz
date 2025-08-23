def divisible_by_5(a_list: list[int]) -> None:
    for i in a_list:
        if i > 150:
            break
        
        if i % 5 == 0:
            print(i)
