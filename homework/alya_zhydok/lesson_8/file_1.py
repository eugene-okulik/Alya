import random
salary = int(input('Enter your salary'))
# print(salary)
bonus = bool(random.choice([True, False]))
# print(bonus)
number = random.randint(1000, 5000)
if bonus is True:
    salary_result = salary + number
else:
    salary_result = salary

print(f"{salary}, {bonus} - '${salary_result}'")
