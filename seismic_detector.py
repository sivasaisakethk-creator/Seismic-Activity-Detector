def on_button_pressed_a():
    music.stop_all_sounds()
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

vibration = 0
z = 0
y = 0
x = 0
WARNING_THRESHOLD = 300
DANGER_THRESHOLD = 700

def on_forever():
    global x, y, z, vibration
    x = abs(input.acceleration(Dimension.X))
    y = abs(input.acceleration(Dimension.Y))
    z = abs(input.acceleration(Dimension.Z))
    vibration = x + y + z - 1024
    if vibration < 0:
        vibration = 0
    serial.write_value("Vibration", vibration)
    if vibration > DANGER_THRESHOLD:
        basic.show_icon(IconNames.SKULL)
        music.play_tone(1000, music.beat(BeatFraction.SIXTEENTH))
        basic.pause(100)
        music.play_tone(1000, music.beat(BeatFraction.SIXTEENTH))
        basic.pause(100)
        music.play_tone(1000, music.beat(BeatFraction.SIXTEENTH))
    elif vibration > WARNING_THRESHOLD:
        basic.show_icon(IconNames.SMALL_DIAMOND)
        music.play_tone(700, music.beat(BeatFraction.QUARTER))
    else:
        basic.show_icon(IconNames.YES)
    basic.pause(100)
basic.forever(on_forever)
