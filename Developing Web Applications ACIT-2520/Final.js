const fs = require("fs").promises;


const listToDict = (list) =>{
    const dataDict = {"medium-roast":0,"dark-roast":0,"blonde":0}
    for(item in list){
        if (list[item] in dataDict) {
            dataDict[list[item]] += 1
    }
}
    return dataDict
}
const viewAllSupply = (coffeeType, data) => {
    if (coffeeType in reference) {
        console.log(data[reference[coffeeType]])
    }
    return data
}
// a function which should return a single number that represents
// how many of that coffee is in stock. 

//You can pass the following items into
// the function: 
// "DR" (for dark-roast)
// "MR" (for medium-roast)
// "B"  (for blonde)

// If a user passes into the function a value that is NOT "DR", "MR", "B", 
// you should consider it an error and tell the user they passed an incorrect
// value into the function, and then stop the program. 

//ex - viewAllSupply("MR");
//-> returns 8


// (2)
const addSupply = (coffeeType, data) => {
    if (coffeeType in reference){
        data[reference[coffeeType]] += 1
    } 
    return data
}
//ex - addSupply("MR");
//-> should add to the end of supply.txt file the coffee type. 
//You can pass the following into
// the function:
// "DR"
// "MR"
// "B"

//⛔️ Warning: even though the user types "DR"..it should add to the end of 
//supply.txt dark-roast, not DR. Same goes with "MR" and "B". 


// (3)
const deleteSupply = (coffeeType, quantity, data) => {
    if (coffeeType in reference){
        if (quantity == "*" || quantity > data[reference[coffeeType]]){
            quantity = data[reference[coffeeType]]
        }
        data[reference[coffeeType]] -= quantity
        console.log(`Remove ${quantity} of ${reference[coffeeType]}`)
    } 
    return data
    
}
//ex - deleteSupply("MR", "*");
//You can pass the following into
// the function:
// ("DR", "*") or ("DR", <number>)
// ("MR", "*") or ("MR", <number>)
// ("B", "*") or ("B", <number>)

// There are 2 things you pass into this function: the type of coffee
// you want to delete, and how many of them you want to delete. 

// If a user passes "*" for the quantity, you should delete ALL the
// instances of the coffee type from the file. 

// If a user passes a number like 3, it means delete only three of them
// from the file. 

// You may safely assume only positive numbers will be passed into the
// function.

// Your delete function should not only perform the delete, but also show
// a message as follows:


// If the function call was: ("DR", "*") then display:
// All Dark Roast coffee(s) deleted.

// If the function call was: ("DR", 3) then display:
// 3 Dark Roast coffee(s) deleted.

// If the function call was: ("B", 1) then display:
// 1 Blonde coffee(s) deleted.

// Edge Cases:

// If the function call was something like ("DR", 5) but
// there are no dark roasts in the supply, then display:
// 0 Dark Roast coffee(s) deleted.

// If the function call was something like ("DR", 300) but
// there are only 5 dark roasts in the supply, then display:
// 5 Dark Roast coffee(s) deleted.

//To demonstrate that your program is working correctly, write the
//following test code below...and make sure each function call executes
//IN ORDER (the sequence matters):
 
//First viewAllSupply for "MR". 
//Then call addSupply one time with "MR".
//Then call viewAllSupply again with "MR".
//Then call deleteSupply with "MR" and 2. 
//Then call viewAllSupply again with "MR".
//Then call deleteSupply with "MR" and *. 
//Then call viewAllSupply again with "MR"
//Finally, print "Program is completed". 
const writeFinal = (data) => {
    fs.writeFile("supply.txt", '')
    for (coffeeType in data){
        for (var i = 0; i < data[coffeeType]; i++){
            fs.appendFile("supply.txt", coffeeType + "\n")
        }
    }
}

const getData = async() => {
    var data = "Program is completed";
    return data;
}



const reference = {"MR": "medium-roast", "DR": "dark-roast","B":"blonde"}
fs.readFile("supply.txt", "UTF-8")
.then(data => data.split(/\r?\n/))
.then(data => listToDict(data))
.then(data => viewAllSupply("MR", data))
.then(data => addSupply("MR", data))
.then(data => viewAllSupply("MR", data))
.then(data => deleteSupply("MR", 2, data))
.then(data => viewAllSupply("MR",data))
.then(data => deleteSupply("MR", "*", data))
.then(data => viewAllSupply("MR",data))
.then(data => writeFinal(data))
.then(data => getData())
.then(data => console.log(data))