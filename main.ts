input.onButtonPressed(Button.B, function () {
    basic.showLeds(`
        . . # . .
        . # . # .
        . . # . .
        # # . . #
        . # # # .
        `)
    music.play(music.stringPlayable("A F E F D G E F ", 340), music.PlaybackMode.InBackground)
    basic.showString("Goodbye!")
})
basic.showNumber(12)
basic.showLeds(`
    . . # . .
    . # . # .
    . . # . .
    # # . . #
    . # # # .
    `)
basic.showIcon(IconNames.Heart)
basic.forever(function () {
    let myVar = 0
    basic.showLeds(`
        . . # . .
        . # . # .
        . . # . .
        # # . . #
        . # # # .
        `)
    if (0 == 45 + 8) {
    	
    } else if (myVar && false) {
    	
    } else {
    	
    }
})
