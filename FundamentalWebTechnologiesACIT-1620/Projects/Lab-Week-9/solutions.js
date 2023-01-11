//part 1

const myArray = [ 2, 5, 8, 10, 15, 20 ]
const failMessage = 'this is not the number you are looking for'

for (const num of myArray) {
    if (num == 10) {
        console.log("The number 10 has been found")
    }else {
        console.log(failMessage)
    }
}
//part 2

const Name = "Caleb"
for (const str of Name) {
    console.log(str)
}

//part 3

const number1 = 12

if (number1 > 10) {
    console.log(`Number too big number is: ${number1}`)
} else if (number1 > 5) {
    console.log("Number is bigger than 5")
} else if (number1 > 1) {
    console.log("Number is bigger than 1")
}

//part 4

let line = "#"
let i = 0

while (i < 7) {
    console.log(line)
    line += "#"
    i += 1
}