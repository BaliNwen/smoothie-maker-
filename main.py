game.splash("Welcom to the smoothie maker!")
game.splash("You thought i was going to make your smoothie?")
game.splash("no. HaHA!") #tease

fruits = ["blueberry" , "mango", "peach", "watermelon", "blackberry", "banana", "pinapple"]

game.splash("Choose from this selection: " + fruits)


def fruit_selector(array_fruit):
    selection = game.ask_for_string("what kind of smoothie would you like?").to_lower_case()
    found = False # if wrong option
    for fruit in array_fruit:
        found = True # if correct option 
        game.splash("You've made a " + fruit + " smoothie" )
        if not found:
            game.splash("We don't have: " + selection + "!" + " choose something else you rat!")

fruit_selector(fruits)