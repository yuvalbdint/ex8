import importlib.util

yuv_path = r"C:\Users\Yuval\PycharmProjects\ex8\aa\yuvSol.py"


def check_single_student(file_path, re) -> list:
    errors = []
    if re:
        errors.append("Re")

    try:
        spec = importlib.util.spec_from_file_location("", file_path)
        a = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(a)
    except Exception as a:
        errors.append("Imp")
        return errors

    # test Minibar

    drinks1 = {'coke': 12, 'rum': 25}
    snacks1 = {'m&m': 10, 'cake': 30}

    mini = None
    try:
        mini = a.Minibar(drinks1, snacks1)

    except Exception as e:
        errors.append("A1")  # cannot create minibar

    if mini is not None:
        mini.eat_a_snack("cake")
        expected = "The minibar contains the drinks: ['coke', 'rum']\nAnd the snacks: ['m&m']\nThe bill for the " \
                   "minibar is: 30.0"

        if repr(mini) != expected:
            errors.append("A2")

        try:
            mini.drink_a_drink("orange juice")
        except ValueError as e:
            expected = "The drink is not in the minibar"
            if e.__str__() != expected:
                errors.append("A3")
        except Exception as e:
            errors.append("A3X")

    return errors


errs = check_single_student(yuv_path, False)
print(errs)

# r1 = a.Room(mini, 2, 23, ["Dana", "Ron"], 5, 2)
# r_better = a.Room(mini, 6, 57, [], 4, 3)
# print(r_better.better_than(r1))
# r_better.check_in(["Amir"])
# r_better.clean()
# print(r_better.clean_level)
#
# # r1.check_in(["Avi", "Hadar"])
#
# print(r1.is_occupied())
#
# r1.check_out()
# print(r1.is_occupied())
#
# r_better.move_to(r1)
# print(r1.satisfaction)
#
# print(r1.guests)
#
# r1.move_to(r_better)
# print(r1.is_occupied())
#
# print(r_better.satisfaction)
# print(r_better.guests)
