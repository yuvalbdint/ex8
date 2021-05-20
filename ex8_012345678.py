''' Exercise #8. Python for Engineers.'''


#########################################
# Question 1 - do not delete this comment
#########################################
class Minibar:
    def __init__(self, drinks, snacks):
        self.drinks = drinks
        self.snacks = snacks
        self.bill = 0.0

    def __repr__(self):
        _drinks = list(self.drinks.keys())
        _snacks = list(self.snacks.keys())
        return "The minibar contains the drinks: {}\nand the snacks: {}\nThe bill for the minibar is: {}".format(
            _drinks, _snacks, self.bill)

    def eat_a_snack(self, snack):
        if snack in self.snacks:
            self.bill += self.snacks.pop(snack)
        else:
            raise ValueError("The snack is not in the minibar")

    def drink_a_drink(self, drink):
        if drink in self.drinks:
            self.bill += self.drinks.pop(drink)
        else:
            raise ValueError("The drink is not in the minibar")


#########################################
# Question 2 - do not delete this comment
#########################################
class RoomError(Exception):
    # A subclass of Exception that defines a new error type
    # DO NOT change this class
    pass


class Room:
    def __init__(self, minibar, floor, number, guests, clean_level, rank, satisfaction=1.0):
        if type(clean_level) != int or type(rank) != int or \
                (type(satisfaction) != int and type(satisfaction) != float):
            raise TypeError()

        if clean_level > 10 or clean_level < 1 or rank > 3 or rank < 1 or satisfaction > 5 or satisfaction < 1:
            raise ValueError()

        self.minibar = minibar
        self.floor = floor
        self.number = number
        self.guests = [guest.lower() for guest in guests]
        self.clean_level = clean_level
        self.rank = rank
        self.satisfaction = float(satisfaction)

    def __repr__(self):
        _guests = "empty" if len(self.guests) == 0 else ", ".join(self.guests)
        return self.minibar.__repr__() + "\nfloor: {}\nnumber: {}\nguests: {}\nclean_level: {}\nrank: {}" \
                                         "\nsatisfaction: {}" \
            .format(self.floor, self.number, _guests, self.clean_level, self.rank, round(self.satisfaction, 1))

    def is_occupied(self):
        return len(self.guests) > 0

    def clean(self):
        self.clean_level = min(10, self.clean_level + self.rank)

    def better_than(self, other):
        if type(other) != Room:
            raise TypeError
        return (self.rank, self.floor, self.clean_level) > (other.rank, other.floor, other.clean_level)

    def check_in(self, guests):
        if self.is_occupied():
            raise RoomError("Cannot check-in new guests to an occupied room")
        self.guests = [guest.lower() for guest in guests]
        self.satisfaction = 1.0

    def check_out(self):
        if not self.is_occupied():
            raise RoomError("Cannot check-out an empty room")
        else:
            self.guests = []

    def move_to(self, other):
        if not self.is_occupied():
            raise RoomError("Cannot move guests from an empty room")
        if other.is_occupied():
            raise RoomError("Cannot move guests into an occupied room")

        other.guests = self.guests.copy()  ### @yuval - test it!!!

        if other.better_than(self):
            other.satisfaction = min(5.0, self.satisfaction + 1.0)
        else:
            other.satisfaction = self.satisfaction

        self.guests = []


#########################################
# Question 3 - do not delete this comment
#########################################
class Hotel:
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms
        self.room_num = len(rooms)

    def __repr__(self):
        occ_num = sum([1 for room in self.rooms if room.is_occupied()])
        return "{} hotel has:\n{} rooms\n{} occupied rooms".format(self.name, self.room_num, occ_num)

    def check_in(self, guests, rank):
        for room in self.rooms:
            if not room.is_occupied() and room.rank == rank:
                room.check_in(guests)
                return room
        return None

    def check_out(self, guest):
        room = self.search_room_with_guest(guest)
        if room is None:
            return None

        room.check_out()
        return room

        return None

    def search_room_with_guest(self, guest):
        guest = guest.lower()
        for room in self.rooms:
            for g in room.guests:
                if g == guest:
                    return room

        return None

    def upgrade(self, guest):
        org_room = self.search_room_with_guest(guest)
        if org_room is None:
            return None

        for room in self.rooms:
            if room.better_than(org_room) and not room.is_occupied():
                org_room.move_to(room)   ## is this what they ment?
                return room

        return None


#########################################
# Question 3 supplement - do not delete this comment
#########################################
def test_hotel():
    m = Minibar({'coke': 10, 'lemonade': 7}, {'bamba': 8, 'mars': 12})
    rooms = [Room(m, 15, 140, [], 5, 1), Room(m, 12, 101, ["Ronen", "Shir"], 6, 2),
             Room(m, 1, 2, ["Liat"], 7, 1), Room(m, 2, 23, [], 6, 3)]
    h = Hotel("Dan", rooms)
    test_sep = '\n------------------'
    print('PRINT h:\n', h, test_sep, sep="")
    print(m)
    print('PRINT h:\n', h, test_sep, sep="")
    print('CALL: h.upgrade("Liat")\n', h.upgrade("Liat"), test_sep, sep="")
    print('CALL: h.check_out("Ronen")\n', h.check_out("Ronen"), test_sep, sep="")
    print('CALL: h.check_out("Ronen")\n', h.check_out("Ronen"), test_sep, sep="")
    print('CALL: h.check_in(["Alice", "Wonder"], 2)\n', h.check_in(["Alice", "Wonder"], 2), test_sep, sep="")
    print('CALL: h.check_in(["Alex"], 3)\n', h.check_in(["Alex"], 3), test_sep, sep="")
    print('PRINT h:\n', h, test_sep, sep="")
    print('CALL: h.check_in(["Oded", "Shani"], 3)\n', h.check_in(["Oded", "Shani"], 3), test_sep, sep="")
    print('CALL: h.check_in(["Oded", "Shani"], 1)\n', h.check_in(["Oded", "Shani"], 1), test_sep, sep="")
    print('CALL: h.check_out("Liat")\n', h.check_out("Liat"), test_sep, sep="")
    print('CALL: h.check_out("Liat")\n', h.check_out("Liat"), test_sep, sep="")
    print('PRINT h:\n', h, test_sep, sep="")


#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################
if __name__ == "__main__":
    test_hotel()
    pass
