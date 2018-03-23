"""attempt to successfully generate a knitting pattern for a square or rectangle
takes gauge_rows and gauge_stitches: gauge_rows = height in rows per 10cm and gauge_stitches = width in stitches per 10cm
generates a knitting pattern for a square or rectangle using the gauge or tension measurements to create
the desired finished size"""


gauge_rows = int(input("How many rows per 10cm in your gauge square? "))
gauge_stitches = int(input("How many stitches per 10cm in your gauge square? "))
finished_width = int(input("How wide would you like the finished square or rectangle to be? (in centimetres) "))
finished_height = int(input("How long would you like the finished square or rectangle to be? (in centimetres) "))
isStockinette = input("Would you like stockinette stitch? (True or False)" )


def kniterate_rectangle(gauge_rows, gauge_stitches, finished_width, finished_height):
    stitch_width = float(100 / gauge_stitches) # this puts it into mm
    stitch_height = float(100 / gauge_rows) # this puts it into mm
    cast_on = int(finished_width * 10 / stitch_width) # but this should round up
    number_of_rows = int(finished_height * 10 / stitch_height)
    return {"cast on": cast_on, "number of rows": number_of_rows}

"""print("width: ", stitch_width, " height: ", stitch_height)
print("cast on: ", cast_on, " knit ", number_of_rows, " number of rows")
print("or turned into integers ", "cast on ", int(cast_on), " knit ", int(number_of_rows), " rows")"""

def print_pattern():
    if isStockinette == "True":
        print("Pattern for a ", finished_width, " by ", finished_height, " Rectangle ")
        print("CO ", cast_on, " stitches")
        print("row 1: knit all stitches")
        print("row 2: purl")
        print("work ", number_of_rows, " rows even")
        print("BO")




