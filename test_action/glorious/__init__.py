def rainbowfier(string):
    colors = [
        "\033[91m",
        "\033[93m",
        "\033[92m",
        "\033[94m",
        "\033[95m",
        "\033[96m",
    ]  # ANSI escape codes for colors

    rainbow_string = ""
    color_index = 0

    for char in string:
        rainbow_string += colors[color_index] + char
        color_index = (color_index + 1) % len(colors)

    return rainbow_string + "\033[0m"  # Reset color after the string
