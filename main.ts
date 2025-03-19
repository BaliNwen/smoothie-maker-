//  return statement / user input
function fruit_selector(array_fruit: string) {
    for (let x of array_fruit) {
        if (x == "" && py.In("", array_fruit)) {
            game.splash("You've made a " + "" + "smoothie!")
        } else if (x) {
            array_fruit.indexOf("") >= 0
        }
        
        //  if value not in list then make them restart
        game.splash("You didn't select anything!")
        game.gameOver(false)
    }
}

game.splash("Welcome to the smoothie maker!")
game.splash("you get to make your own smoothie!")
game.splash("Here are your ingredients!")
let array_fruit = ["blueberry", "mango", "peach", "watermelon", "blackberry", "banana", "pineapple"]
//  array of fruit
game.splash(array_fruit)
fruit_selector(game.askForString("what would you like to add to your drink?"))
