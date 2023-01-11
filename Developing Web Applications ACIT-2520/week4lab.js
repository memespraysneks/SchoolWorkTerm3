const fs = require("fs")
const { off } = require("process")

const writeFileP = (fName, fContent) => {
    return new Promise((resolve, reject) => {
        fs.writeFile(fName, fContent, (err) => {
            if (err) {
                reject(err)
            } else{
                resolve()
            }
        })
    })
}

const readFileP = (fName) => {
    return new Promise((resolve, reject) => {
        fs.readFile(fName, "utf8", (err, data) => {
            if (err) {
                reject(err);
            } else{
                resolve(data.split("\r\n"));
            }
        });
    });
};

const colonManipulator = (userList) => {
    const listOfUsersColons = []
    for (item of userList){
            colons = item.split(":")
            listOfUsersColons.push(colons[0])
    }
    return listOfUsersColons
}

const register = (username, password, userList) => {
    if (!((userList.includes(username)))){
        fs.appendFile("database.txt", `\n${username}:${password}`,(err)=>{})
    }
}


readFileP("database.txt")
    .then(data => colonManipulator(data))
    .then(data => register("caleb2","myAss", data))
    .catch()