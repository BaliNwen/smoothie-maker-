# return statement / user input
def fruit_selector(array_fruit: str):
    # if users input inside the list than print the value selected
    if array_fruit.index_of("") >= 0:
        game.splash("You've made a " + return '' :in array_fruit  + "smoothie!")
    elif array_fruit.index_of("") < 0:
        # if value not in list then make them restart
        game.splash("You didn't select anything!")
        game.game_over(False)
    return array_fruit
game.splash("Welcome to the smoothie maker!")
game.splash("you get to make your own smoothie!")
game.splash("Here are your ingredients!")
array_fruit = ["blueberry",
    "mango",
    "peach",
    "watermelon",
    "blackberry",
    "banana",
    "pineapple"]
# array of fruit
game.splash(array_fruit)
fruit_selector(game.ask_for_string("what would you like to add to your drink?"))