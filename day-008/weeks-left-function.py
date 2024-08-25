def life_in_weeks(age):
    target_age = 90
    years_left = target_age - age
    weeks_left = years_left * 52
    print(f"You have {weeks_left} weeks left.")

life_in_weeks(42)