############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        self.pairings = [] # just chainge location of this code.
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless 
        self.is_bestseller = is_bestseller
        self.name = name

        """Initialize a melon."""

        
       

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        # for pair in pairing:
        #     self.pairings.append(pair)  ///// this is a comment for my code

        self.pairings.append(pairing)  # new code 
        
    

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code
        print(f"Code updated to {new_code}")

    # def __repr__(self):
    #     return f'Melon name is {self.name} & Melon code is {self.code} '


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk_melon = MelonType("musk", "Muskmelon", 1998, "green", True, True)
    musk_melon.add_pairing("mint")
    all_melon_types.append(musk)

    casaba_melon = MelonType("cas", "Casaba", 2003, "orange", False, False)
    casaba_melon.add_pairing("mint///strawberries")
    casaba_melon.add_pairing("mint///strawberries") # added this code
    all_melon_types.append(casaba_melon)

    crenshaw_melon = MelonType("cren", "Crenshaw", 1996, "green", False, False)
    crenshaw_melon.add_pairing("prosciutto")
    all_melon_types.append(crenshaw_melon)

    yellow_watermelon = MelonType("yw", "Yellow Watermelon", 2013, "yellow", False, True)
    yellow_watermelon.add_pairing("ice cream")
    all_melon_types.append(yellow_watermelon)

    return all_melon_types

#melon_types = make_melon_types()

def print_pairing_info(melon_types):
    """
    Prints information about each melon type's pairings
    """
    for melon in melon_types:
       print(f"{melon.name} pairs with")
       for pairing in melon.pairings:
        print(f"- {pairing}")
    print()
   


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    melons_by_id = {}
    for melon in melon_types:
        if melon.code not in melons_by_id:
            melons_by_id[melon.code] = melon

    return melons_by_id


#  First code review checkpoint

############
# Part 2   #
############

class Melon:
    """A melon in a melon harvest."""
    def __init__(self, melon_type, shape_rating, color_rating, field, harvester):
        # Initialize a melon instance.
        self.melon_type = melon_type
        self.shape_rating  = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester

    def is_sellable(self):
            """Determine whether this melon can be sold."""
        if self.shape_rating > 5 and self.color_rating > 5 and self.field != 3:
            return True
        else:
            return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melons_by_id = make_melon_type_lookup(melon_types)
    # Fill in the rest
    melon_1 = Melon(melons_by_id["yw"], 8, 7, 2, "Sheila")
    melon_2 = Melon(melons_by_id["yw"], 3, 4, 2, "Sheila")
    melon_3 = Melon(melons_by_id["yw"], 9, 8, 3, "Sheila")
    melon_4 = Melon(melons_by_id["cas"], 10, 6, 35, "Sheila")
    melon_5 = Melon(melons_by_id["cren"], 8, 9, 35, "Michael")
    melon_6 = Melon(melons_by_id["cren"], 8, 2, 35, "Michael")
    melon_7 = Melon(melons_by_id["cren"], 2, 3, 4, "Michael")
    melon_8 = Melon(melons_by_id["musk"], 6, 7, 4, "Michael")
    melon_9 = Melon(melons_by_id["yw"], 7, 10, 3, "Michael")

    melons = [
        melon_1,
        melon_2,
        melon_3,
        melon_4,
        melon_5,
        melon_6,
        melon_7,
        melon_8,
        melon_9,
    ]

    return melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
    for melon in melons:
        harvested_by = f"Harvested by {melon.harvester}"
        field_num = f"Field #{melon.field}"
        status = "CAN BE SOLD" if melon.is_sellable() else "NOT SELLABLE"
        print(f"{harvested_by} from {field_num} {status}")
