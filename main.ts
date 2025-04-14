//  (glorified print statement) project
function fruit_selection(array_fruit: any[]) {
    
    let choice = game.askForString("what kind of smoothie would you like to make?").toLowerCase()
    //  makes it auto lowercase
    //  loop through each fruit in the list
    for (let fruit of array_fruit) {
        if (fruit == choice) {
            encontro = true
            game.splash("you've made a " + ("" + ("" + fruit)) + " smoothie!")
            game.splash("goodbye.")
            game.gameOver(true)
        }
        
    }
    //  if no match found: error msg = true
    if (!encontro) {
        game.splash("we dont have " + choice + "." + "please choose something else. ")
        game.splash("stop trolling and choose something weirdo.")
        game.gameOver(false)
    }
    
}

let encontro = false
game.splash("welcome to the smoothie maker ladies and gentlemen.")
game.splash("you may commence your smoothie making vermin.")
let froots = ["blueberry", "mango", "peach", "watermelon", "blackberry", "banana", "pineapple"]
game.splash("here are your ingredients: blueberry, mango, peach, watermelon, blackberry, banana, pineapple")
game.splash("please choose an option to make a smoothie.")
fruit_selection(froots)
