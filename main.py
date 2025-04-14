# (glorified print statement) project
def fruit_selection(array_fruit: List[any]):
    global encontro
    choice = game.ask_for_string("what kind of smoothie would you like to make?").to_lower_case()
    # makes it auto lowercase
    # loop through each fruit in the list
    for fruit in array_fruit:
        if fruit == choice:
            encontro = True
            game.splash("you've made a " + ("" + str(fruit)) + " smoothie!")
            game.splash("goodbye.")
            game.game_over(True)
    # if no match found: error msg = true
    if not (encontro):
        game.splash("we dont have " + choice + "." + "please choose something else. ")
        game.splash("stop trolling and choose something weirdo.")
        game.game_over(False)
encontro = False
game.splash("welcome to the smoothie maker ladies and gentlemen.")
game.splash("you may commence your smoothie making vermin.")
froots = ["blueberry",
    "mango",
    "peach",
    "watermelon",
    "blackberry",
    "banana",
    "pineapple"]
game.splash("here are your ingredients: blueberry, mango, peach, watermelon, blackberry, banana, pineapple")
game.splash("please choose an option to make a smoothie.")
fruit_selection(froots)