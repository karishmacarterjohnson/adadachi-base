def continue_activity():
    decision = input("would you like to continue? y or n")
    if decision.lower() == "n":
        decision = False
    else:
        decision = True
    return decision