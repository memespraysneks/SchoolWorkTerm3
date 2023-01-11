const fs = require("fs").promises;

const itemTypeSeperation = (itemList) => {
    seperatedList = {}
    for (item in itemList) {
        split = itemList[item].split(",")
        if(seperatedList.hasOwnProperty(split[0])){
            seperatedList[split[0]].push(split.slice(1))
        } else {
            seperatedList[split[0]] = [split.slice(1)]
        }
    }
    return (seperatedList)
}


fs.readFile("menu.csv", "UTF-8")
.then(data => data.split("\r\n"))
.then(data => itemTypeSeperation(data))
.then(data => {for(mealType in data){
    mealString = ""
    for (item in data[mealType]){
        mealString = mealString + data[mealType][item][2] + "  " + data[mealType][item][0] + ", " + data[mealType][item][1] + "\r\n"
    }
    fs.appendFile("menu.txt", `*  ${mealType.charAt(0).toUpperCase()}${mealType.slice(1)} Items  *\r\n${mealString}`)
    
}console.log("file created!")})
.catch(err => console.log(err))