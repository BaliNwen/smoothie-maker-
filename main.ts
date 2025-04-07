game.splash("Welcom to the smoothie maker!")
game.splash("You thought i was going to make your smoothie?")
game.splash("no. HaHA!")
// tease
let fruits = ["blueberry", "mango", "peach", "watermelon", "blackberry", "banana", "pinapple"]
game.splash("Choose from this selection: " + fruits)
function fruit_selector(array_fruit: any[]) {
    let selection = game.askForString("what kind of smoothie would you like?").toLowerCase()
    let found = false
    //  if wrong option
    for (let fruit of array_fruit) {
        found = true
        //  if correct option 
        game.splash("You've made a " + fruit + " smoothie")
        if (!found) {
            game.splash("We don't have: " + selection + "!" + " choose something else you rat!")
        }
        
    }
}

fruit_selector(fruits)
