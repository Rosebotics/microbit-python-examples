import microbit as mb


def main():
    # mb.display.scroll("Dave Fisher")
    # mb.display.show(mb.Image("60006:06060:00900:03030:20002"))
    # mb.display.show(mb.Image.ALL_CLOCKS, loop=True, delay=100)
    # for i in range(3):
    #     mb.sleep(2)
    #     sinkingBoat()
    while True:
        if mb.button_a.is_pressed() and mb.button_b.is_pressed():
            break
        if mb.button_a.was_pressed():
            # Does a 1.6 second animation of 4 images (default delay is 400ms)
            mb.display.show([mb.Image.ARROW_N, mb.Image.ARROW_E,
                             mb.Image.ARROW_S, mb.Image.ARROW_W])
            # mb.sleep(2000)
        if mb.button_b.was_pressed():
            mb.display.show(mb.Image.ANGRY)  # Single image needs a sleep after
            mb.sleep(2000)
        # if mb.pin7.read_digital() == 0:  # These didn't really work
        #    mb.display.scroll("Pressed")
        # if mb.pin0.is_touched():
        #    mb.display.show(mb.Image.HAPPY)
        #    mb.sleep(2000)

        reading = mb.accelerometer.get_x()
        if reading > 100:
            mb.display.show("R")
        elif reading < -100:
            mb.display.show("L")
        else:
            mb.display.show("-")
        mb.sleep(200)

    mb.display.scroll("Goodbye")


def sinkingBoat():
    boat1 = mb.Image("05050:"
                     "05050:"
                     "05050:"
                     "99999:"
                     "09990")

    boat2 = mb.Image("00000:"
                     "05050:"
                     "05050:"
                     "05050:"
                     "99999")

    boat3 = mb.Image("00000:"
                     "00000:"
                     "05050:"
                     "05050:"
                     "05050")

    boat4 = mb.Image("00000:"
                     "00000:"
                     "00000:"
                     "05050:"
                     "05050")

    boat5 = mb.Image("00000:"
                     "00000:"
                     "00000:"
                     "00000:"
                     "05050")

    boat6 = mb.Image("00000:"
                     "00000:"
                     "00000:"
                     "00000:"
                     "00000")

    all_boats = [boat1, boat2, boat3, boat4, boat5, boat6]
    mb.display.show(all_boats, delay=200)


main()
