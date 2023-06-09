############
# Part 1   #
############

from sys import argv


class MelonType:
    """A species of melon at a melon farm."""



    def __init__(self,
                 code,
                 first_harvest,
                 color,
                 is_seedless,
                 is_bestseller,
                 name
                 ):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    muskmelon = MelonType("musk", # Reporting code
                          1998, # First harvest year
                          "green", # color
                          True, # is seedless
                          True, # is best seller
                          "Muskmelon" # Name
                          ) 
    
    muskmelon.add_pairing("mint")
    all_melon_types.append(muskmelon)


    casaba = MelonType("cas", # Reporting code
                          2003, # First harvest year
                          "orange", # color
                          True, # is seedless
                          False, # is best seller
                          "Casaba" # Name
                          )
    
    casaba.add_pairing("strawberries")
    casaba.add_pairing("mint")
    all_melon_types.append(casaba)
    

    crenshaw = MelonType("cren", # Reporting code
                          1996, # First harvest year
                          "green", # color
                          False, # is seedless
                          False, # is best seller
                          "Crenshaw", # Name
                          )
    
    crenshaw.add_pairing("prosciutto")
    all_melon_types.append(crenshaw)

    yellowmellon = MelonType("yw", # Reporting code
                          2013, # First harvest year
                          "yellow", # color
                          True, # is seedless
                          True, # is best seller
                          "Yellow Watermelon" # Name
                          )
    
    yellowmellon.add_pairing("ice cream")
    all_melon_types.append(yellowmellon)
    
    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for pairing in melon.pairings:
            print(f"- {pairing}")
    
        print() # Adding a newline for formatting



def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dictionary = {}

    for melon in melon_types:
        melon_dictionary[melon.code] = melon

    return melon_dictionary


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    def __init__(self,
                 melon_type,
                 shape_rating,
                 color_rating,
                 from_field,
                 harvested_by
                 ):
        
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.from_field = from_field
        self.harvested_by = harvested_by

    def is_sellable(self):
        if self.shape_rating and self.color_rating > 5 and self.from_field != 3:
            return True
        else:
            return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    all_melons = []
    melons_by_id = make_melon_type_lookup(melon_types)

    melons_string = (   "Shape 8 Color 7 Type yw Harvested By Sheila Field #2\n"
                        "Shape 3 Color 4 Type yw Harvested By Sheila Field #2\n"
                        "Shape 9 Color 8 Type yw Harvested By Sheila Field #3\n"
                        "Shape 10 Color 6 Type cas Harvested By Sheila Field #35\n"
                        "Shape 8 Color 9 Type cren Harvested By Michael Field #35\n"
                        "Shape 8 Color 2 Type cren Harvested By Michael Field #35\n"
                        "Shape 2 Color 3 Type cren Harvested By Michael Field #4\n"
                        "Shape 6 Color 7 Type musk Harvested By Michael Field #4\n"
                        "Shape 7 Color 10 Type yw Harvested By Sheila Field #3"
                    )

    for line in melons_string.splitlines():
        word = line.strip().split(" ")

        melon = Melon(melons_by_id[word[5]],    # MelonType
                    int(word[1]),                    # Shape Rating
                    int(word[3]),                    # Color Rating
                    int(word[10].replace("#", "")),  # Field Harvested From
                    word[8]                     # Harvested By
                      )
        
        all_melons.append(melon)

    return all_melons


    # melon_1 = Melon(melons_by_id["yw"],     # MelonType
    #                 8,                      # Shape Rating
    #                 7,                      # Color Rating
    #                 2,                      # Field Harvested From
    #                 "Sheila"                # Harvested By
    #                 )
    
    # all_melons.append(melon_1)

def make_melons_from_file(melon_types, file_path):
    """Returns a list of Melon objects."""

    all_melons = []
    melons_by_id = make_melon_type_lookup(melon_types)


    with open(file_path, "r") as file:

        for line in file:
            word = line.strip().split(" ")

            melon = Melon(melons_by_id[word[5]],    # MelonType
                        int(word[1]),                    # Shape Rating
                        int(word[3]),                    # Color Rating
                        int(word[11].replace("#", "")),  # Field Harvested From
                        word[8]                     # Harvested By
                        )
            
            all_melons.append(melon)

    return all_melons



def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable():
            sellable_text = "(CAN BE SOLD)"
        else:
            sellable_text = "(NOT SELLABLE)"
        
        print(f"Harvested by {melon.harvested_by} " \
              f"{bold_green}from {bold_blue}Field {green}{melon.from_field}{reset_text} " \
              f"{sellable_text}")


print_pairing_info(make_melon_types())


#print(make_melon_type_lookup(make_melon_types()))


print("The dictionary that was created:")
for code, melon in make_melon_type_lookup(make_melon_types()).items():
    print (  f"Reportding Code: {code}\n"
           + f"Name: {melon.name}\n"
           + f"Color: {melon.color}\n"
           + "\n"
           + "~" * 20
           + "\n"
           )
    

if __name__ == "__main__":

    input_file_path = argv[1]

    bold_green = "\033[1;32m"
    bold_blue = "\033[1;34m"
    green = "\033[0;32m"
    reset_text = "\033[0m"

    get_sellability_report(make_melons_from_file(make_melon_types(), input_file_path))