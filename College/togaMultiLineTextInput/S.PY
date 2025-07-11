import os
os.environ['TOGA_BACKEND'] = 'toga_cocoa' 

import toga


def button_handler(widget):
    print("hello")


def build(app):
    box = toga.Box()

    button = toga.Button("Hello world", on_press=button_handler)
    button.style.margin = 50
    button.style.flex = 1
    box.add(button)

    return box


def main():
    return toga.App("First App", "org.beeware.toga.examples.tutorial", startup=build)


if __name__ == "__main__":
    main().main_loop()