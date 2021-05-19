import ex8_012345678 as a

drinks1 = {'coke': 12, 'rum': 25}
snacks1 = {'m&m': 10, 'cake': 30}
mini = a.Minibar(drinks1, snacks1)

r1 = a.Room(mini, 2, 23, ["Dana", "Ron"], 5, 2)
r_better = a.Room(mini, 6, 57, [], 4, 3)
print(r_better.better_than(r1))

r_better.check_in(["Amir"])
r_better.clean()
print(r_better.clean_level)

# r1.check_in(["Avi", "Hadar"])

print(r1.is_occupied())

r1.check_out()
print(r1.is_occupied())

r_better.move_to(r1)
print(r1.satisfaction)

print(r1.guests)

r1.move_to(r_better)
print(r1.is_occupied())

print(r_better.satisfaction)
print(r_better.guests)
