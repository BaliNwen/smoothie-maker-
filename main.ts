function fruit_selection(array_fruit: any[]) {
    
    let choice = game.askForString("what kind of smoothie would you like to make?").toLowerCase()
    //  loop through each fruit in the list
    for (let fruit of array_fruit) {
        if (fruit == choice) {
            found = true
            game.splash("you've made a " + ("" + fruit) + " smoothie!")
            game.splash("goodbye.")
            game.gameOver(true)
        }
        
    }
    //  if no match found: error msg = true
    if (!found) {
        game.splash("we dont have " + choice + "." + "Please choose something else. ")
        game.splash("stop trolling and choose something.")
        game.gameOver(false)
    }
    
}

let found = false
game.splash("welcome to the smoothie maker ladies and gentlemen.")
game.splash("you may commence your smoothie making")
let froots = ["blueberry", "mango", "peach", "watermelon", "blackberry", "banana", "pineapple"]
game.splash("here are your ingredients: blueberry, mango, peach, watermelon, blackberry, banana, pineapple")
game.splash("please choose an option to choose from.")
fruit_selection(froots)
