



def test_dict():
    me = {
        "first": "Derek",
        "last": "Urruita",
        "age": 22,
        "hobbies": [],
        "address": {
            "street": "mesa",
            "city": "oceanside"
        },
        "another" : 12,
    }

    print(me["first"] + " " + me["last"])

    print(f"My age is: " + str(me["age"]))
    print(f"My age is: {me['age']}") 

    address = me["address"]
    print(type(address))
    print(address["street"])

    print(me["address"]["city"])

    me["color"] = "red"

    me["age"] = 22

    # check if a key exists in a dictionary
    if "age" in me: 
        print("Age exists")


print("---- Dictionary Test ----")
test_dict()