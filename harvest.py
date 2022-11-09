############
# Part 1   #
############

#We’ll also create one relationship between two classes.
#ask later: num = int(num) <---int is a constructor...this is a built-in conversion function


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon. 

        THIS is the dunder

        attribute/data argument 1 will be updated...idk how yet...explicit/implicit, but through a function (parameters or none)

        example code instantiate: watermelon = melonType(123124, hi, 1998, blue, mint, seedy, not popular)
        """
        self.pairings = [] #dont delete or mess with this, this could have been a dummy one, like something couldve been hardcoded as a great pairing for all melons

        #those arguments are assigned as attributes (hint: use self!)
        self.code=code
        self.first_harvest=first_harvest
        self.color=color
        self.is_seedless=is_seedless
        self.is_bestseller=is_bestseller
        self.name=name
        print (f"this is a {MelonType}")
        
    #making parameter types explicitly in the functions vs the class def
    #method 2
    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list.

        takes a list of strings as pairings
        Both of these methods will mutate existing attributes using the self parameter to each method.
        
        """

        self.pairings.extend(pairing) #<----pairings is an attribute of an already definiend class, 
                                        #and since its also a LIST as defined in class MelonType, its attribute is a list method
                                        #.extend SPECIFICALLY so that it concatenates the two lists into one


                                        #$watermelon = melonType(123124, hi, 1998, blue, mint, seedy, not popular) #<--watermelon object and var
                                        #$watermelon.pairings
                                        #$ [].append()                       #<---prints empty bc its empty in the init





    #method 3
    def update_code(self, new_code):
        """Replace the reporting code with the new_code.
        
        Both of these methods will mutate existing attributes using the self parameter to each method.
        """
        self.code = new_code

        # Fill in the rest






















#---------------NOT A PART OF THE CLASS MELON TYPE------------------------
def make_melon_types():
    """Returns a list of current melon types."""

    #hardcode all 6
    #self, code, first_harvest, color, is_seedless, is_bestseller, name
    muskmelon = MelonType('musk', '1998', 'green', True, True, 'muskmelon')
    casaba = MelonType('cas', '2003', 'orange', False, False, 'casaba')
    crenshaw = MelonType('cren', '1996', 'green', False, False, 'crenshaw')
    yellow_watermelon = MelonType('yw', '2013', 'yellow', False, True, 'yellow watermelon')

    muskmelon.add_pairing(['mint'])
    casaba.add_pairing(['mint', 'strawberies'])
    crenshaw.add_pairing(['proscuitto'])
    yellow_watermelon.add_pairing(['ice cream'])

    all_melon_types = [muskmelon, casaba, crenshaw, yellow_watermelon]

    return all_melon_types
 
def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings.
    Create a function called print_pairing_info that takes a list of MelonType objects as an argument, 
    identical to what make_melon_types returns. This function should simply print out each melon type’s 
    pairings. It should return None. The output should look like this:
    """
    for i in melon_types:
        print (f"{i.name} pairs with")
        for p in i.pairings: #<-----reference init
            print (f"- {p}.")






def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code.
    list manip <---melons come from make melon types ..........dict manip <------create it, 
    
    #$melon_type = make_melon function
    #now...
    #$make_melon_type_lookup(melon_type) <-passed in a whole functions return value, bc THAT info is what drives this function

    # Create a function called make_melon_type_lookup that takes in a list of MelonType 
    # objects as an argument, identical to what make_melon_types returns. 
    # This function should return a dictionary whose keys are reporting codes 
    # (as strings) and whose values are the appropriate melon type instance for that reporting code."""
    melons = {} #must assign x to keys in dictionary
    
    for i in melon_types:
        melons[i.code] = i #indexing via "name" NOT index.....melons['musk']......"i.code == 'musk'" <---dynamic "
        
    
    print(melons)

    return melons






































############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
