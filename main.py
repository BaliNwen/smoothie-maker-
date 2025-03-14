game.splash("Welcome to the smoothie maker!")
game.splash("you get to make your own smoothie!")
game.splash("Here are your ingredients!")
array_fruit = ["blueberry", "mango", "peach", "watermelon", "blackberry", "banana", "pineapple"] #array of fruit

game.splash(array_fruit)

fruit_selector(game.ask_for_string("what would you like to add to your drink?"))



def fruit_selector(array_fruit: str): # if users input inside the list than print the value selected
    if " " in array_fruit:
        game.splash("You've made a " + "" + "smoothie!" )
    elif "" not in array_fruit: # if value not in list then make them restart 
        game.splash("You didn't select anything!")
        game.game_over(False)

fruit_selector(game.ask_for_string("what would you like to add to your drink?")) #return statement / user input        
        


# displays fruits

