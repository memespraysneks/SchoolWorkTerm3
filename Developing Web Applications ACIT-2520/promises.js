const multiplier = (num1, num2) => {
    return new Promise((resolve, reject) => {
        if(typeof(num1) != "number" || typef(num2) != "number"){
            reject("Must pass numbers")
        } else {
            resolve(num1*num2)
        }
    })
}

multiplier(3,4)
.then((value) => console.log(value))
.catch((err) => console.log(err))