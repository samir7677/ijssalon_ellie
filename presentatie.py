def presenteert(dictionary , totaal):
    for key,value in dictionary.items():
        print(f"{key} : {value}euro")
    print("=" * 26)
    print(f"totaal : {totaal}euro")

mijn_dict = {"vis" : 10, "vlees" : 25, "overig" : 15}

totaal = 50

presenteert(mijn_dict, totaal)

