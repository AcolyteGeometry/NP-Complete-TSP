## @package: Utils.MathHelpers
#  Math helpers for calculating various parts of the TSP


## Class contining methods related to number format conversion
#  for example changing a Float into rounded Integer.
class MathHelpers():

    ## The Constructor.
    def __init__(self):
        pass # Do nothing.

    ## String to integer
    #  @type self: ConvertMath
    #  @param self: The object
    #
    #  @type str: string
    #  @param str: the integer string to convert
    #
    #  @rtype: int
    #  @return: The integer from string or 0 on error.
    def stoi(self, str):
        if (str.isdigit()):
            str = int(str)
            return str
        return 0

    ## Converts a float to a rounded integer
    # @type self: ConvertMath
    # @param self: The object.
    #
    # @type fl: Float, String
    # @param fl: Float to convert to integer
    #
    # @rtype: Integer
    # @return: An integer rounded to one place, or 0 if input is invalid.
    def floatToInt(self, fl):
        if(isinstance(fl, float)): # If this is a float
            if(fl.is_integer()): # If it is a whole number return as integer;
                return int(fl)
            else: # Otherwise split at the decimal.
                intarr = str(fl).split(".")
                if(int(intarr[1]) >=5): # Read 1/10ths place, check if >= 5.
                    return int(intarr[0]) + 1 # Return integer rounded up.
                else:
                    return int(intarr[0]) # Otherwise return integer rounded down.
        elif(isinstance(fl, str)): # If float is a string, convert to float and recurse.
            return self.floatToInt(float(fl))
        elif(isinstance(fl, int)): # If float is already an integer just return it.
            return fl
        return 0 # Return 0 if the float is invalid.