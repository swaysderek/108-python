



def younger_person():
    ages = [12,42,32,50,56,14,78,30,51,89,12,38,67,10]

    solution = ages[0]
    for age in ages:
        if age < solution:
            solution = age
        
    print(solution)


def statistics():
    data = [12,-1,123,345,412,4.55,123,23.4,123,4587,-129,94,956,14565,32, 0.001, 123]

    count = 0
    total = 0
    for num in data:
        count = count + 1
        total = total + num

    print(f"1 solution is: {count}")
    print(f"1 solution is: {len(data)}")
    print(f"1 solution is: {total}")


def print_some_nums():
    
    for y in range(10):
        print( (num + 1) * 10)

    for num in range(1, 11):
        print(num * 10)

    for x in range(10, 110, 10):
        print(x)


print("Tests test test")
younger_person()
statistics()