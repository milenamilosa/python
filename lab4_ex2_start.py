### function definition ###

def inch_to_cm(inch_amount):
    cm_amount = inch_amount * 2.54
    #print( inch_amount, "inches equals", cm_amount, "centimeters" )
    return cm_amount

def calc_price(fabric_type, length):
    if fabric_type == "thin":
        price = 1.2 * length
    else:
        price = 3 * length
    print( "the price is €", price )

### main program ###

length2 = inch_to_cm(20)
calc_price("thin", length2)