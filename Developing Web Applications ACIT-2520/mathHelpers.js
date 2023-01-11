const squareRoot = (num)=> {
    return Math.sqrt(num)
}

const square = (num) => {
    return Math.pow(num, 2)
}

const distance = (x1, y1, x2, y2) => {
    return squareRoot((square(x2 - x1)) + (square(y2 - y1)))
}
    
module.exports = {distance}