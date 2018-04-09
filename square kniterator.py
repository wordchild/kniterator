"""attempt to successfully generate a knitting pattern for a square or rectangle
takes gauge_rows and gauge_stitches: gauge_rows = height in rows per 10cm and gauge_stitches = width in stitches per 10cm
generates a knitting pattern for a square or rectangle using the gauge or tension measurements to create
the desired finished size"""

print("Welcome to the Kniterator Pattern Generator!")
print("Please enter your gauge swatch information and desired finished size to knit a square or a rectangle")

gauge_rows = float(input("How many rows per 10cm in your gauge square? "))
gauge_stitches = float(input("How many stitches per 10cm in your gauge square? "))
finished_width = float(input("How wide would you like the finished square or rectangle to be? (in centimetres) "))
finished_height = float(input("How long would you like the finished square or rectangle to be? (in centimetres) "))

stitch_width = float(10 / gauge_stitches)
stitch_height = float(10 / gauge_rows)
cast_on = int(finished_width / stitch_width) # but this should round up
number_of_rows = int(finished_height / stitch_height)

# square knitting pattern in stockinette

if finished_height == finished_width:
    print("Pattern for a ", finished_width, " by ", finished_height, " square")
    print("CO ", cast_on, " stitches")
    print("Row 1: knit all stitches")
    print("Row 2: purl all stitches")
    print("Repeat 1 and 2 for ", number_of_rows, " rows")
    print("Bind off all stiches")

# rectangle knitting pattern in stockinette

elif finished_height != finished_width:
    print("Pattern for a ", finished_width, " by ", finished_height, " rectangle")
    print("CO ", cast_on, " stitches")
    print("Row 1: knit all stitches")
    print("Row 2: purl all stitches")
    print("Repeat 1 and 2 for ", number_of_rows, " rows")
    print("Bind off all stiches")

else:
    print("I'm sorry but I don't understand - would you like to knit a square or a rectangle?")





