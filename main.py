def on_button_pressed_b():
    basic.show_leds("""
        . . # . .
        . # . # .
        . . # . .
        # # . . #
        . # # # .
        """)
    music.play(music.string_playable("A F E F D G E F ", 340),
        music.PlaybackMode.IN_BACKGROUND)
    basic.show_string("Goodbye!")
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_number(12)
basic.show_leds("""
    . . # . .
    . # . # .
    . . # . .
    # # . . #
    . # # # .
    """)

def on_forever():
    myVar = 0
    basic.show_leds("""
        . . # . .
        . # . # .
        . . # . .
        # # . . #
        . # # # .
        """)
    if 0 == 45 + 8:
        pass
    elif myVar and False:
        pass
    else:
        pass
basic.forever(on_forever)
