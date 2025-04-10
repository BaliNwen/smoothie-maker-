game.splash("welcome to the smoothie maker ladies and gentlemen.")
game.splash("you may comence your smoothie making")
froots = ["blueberry", "mango", "peach", "watermelon", "blackberry", "banana", "pineapple"]
game.splash("here are your ingredients: blueberry, mango, peach, watermelon, blackberry, banana, pineapple")
game.splash("please choose an option to choose from.")

def fruit_selection(array_fruit):
    # ask for input & convert it to Lcase
    choice = game.ask_for_string("what kind of smoothie would you like to make?").toLowerCase()
    found = False
    # loop through each fruit in the list
    for fruit in array_fruit:
        if fruit == choice:
            found = True
            game.splash("you've made a " + fruit + " smoothie!")
            game.splash("goodbye.")
            game.game_over(True)
    # if no match found: error msg = true
    if not found:
        game.splash("we do not provide " + choice + "." + "Please choose something else. ")
        game.splash("stop trolling and choose something.")
        game.game_over(False)

fruit_selection(froots)