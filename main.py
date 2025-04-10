def fruit_selection(array_fruit: List[any]):
    global found
    choice = game.ask_for_string("what kind of smoothie would you like to make?").to_lower_case()
    # loop through each fruit in the list
    for fruit in array_fruit:
        if fruit == choice:
            found = True
            game.splash("you've made a " + str(fruit) + " smoothie!")
            game.splash("goodbye.")
            game.game_over(True)
    # if no match found: error msg = true
    if not (found):
        game.splash("we dont have " + choice + "." + "Please choose something else. ")
        game.splash("stop trolling and choose something.")
        game.game_over(False)
found = False
game.splash("welcome to the smoothie maker ladies and gentlemen.")
game.splash("you may commence your smoothie making")
froots = ["blueberry",
    "mango",
    "peach",
    "watermelon",
    "blackberry",
    "banana",
    "pineapple"]
game.splash("here are your ingredients: blueberry, mango, peach, watermelon, blackberry, banana, pineapple")
game.splash("please choose an option to choose from.")
fruit_selection(froots)