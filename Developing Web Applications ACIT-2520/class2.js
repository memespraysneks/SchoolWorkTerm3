function cb(err, result){
    if (err == null){
        console.log(result)
    } else {
        console.log(err)
    }
}

function multiply(number1, number2, callback){
    setTimeout(function (){
        if (typeof number1 !== "number" || typeof number2 !== "number"){
            callback("You must input a number", null)
        } else {
            let num1 = parseInt(number1)
            let num2 = parseInt(number2)
            const final = num1 * num2
            callback(null, final)
        }
    })
}
multiply(20,2,cb)

