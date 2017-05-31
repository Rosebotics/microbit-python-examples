import microbit as mb


def main():
    print("David Fisher can write Python!")
    # mb.display.scroll("Dave Fisher")
    # mb.display.show(mb.Image.HAPPY)
    # mb.display.show([mb.Image.ARROW_N, mb.Image.ARROW_E,
    #                  mb.Image.ARROW_S, mb.Image.ARROW_W])
    # print("Starting an infinite loop")
    # mb.display.show(mb.Image.ALL_CLOCKS, loop=True)
    boat = mb.Image("05050:"
                    "05050:"
                    "05050:"
                    "99999:"
                    "09990")
    mb.display.show(boat)
    
    
main()
