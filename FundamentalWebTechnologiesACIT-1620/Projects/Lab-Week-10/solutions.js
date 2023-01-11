//part 1

const numbersList = [ 3, 5, 8, 22, 6, 43, 50, 21, 28, 14, 2, 30, 16, 36, 7 ]
const evenNumbersList = []

for (let number in numbersList) {
    if (numbersList[number] % 2 === 0) {
        evenNumbersList.push(numbersList[number])
    }
}

console.log(evenNumbersList)

//part 2

const students = [
    { name: "Tasha", grades: [ 80, 67, 75, 62 ] },
    { name: "Tuvok", grades: [ 90, 88, 91, 92 ] },
    { name: "Dax", grades: [ 88, 90, 89, 85 ] },
    { name: "Neelix", grades: [ 60, 54, 48, 50 ] }
  ]
  
  const studentsScholarship = []
  
  for (let student in students) {
    let gradelist = students[student].grades
    let average = 0
    for (let grades in gradelist) {
        average += gradelist[grades]
    }
    average /= 4
    if (average >= 80){
        let temp = {name: students[student].name, gradeAvg: average}
        studentsScholarship.push(temp)
    }
  }

console.log(studentsScholarship)

//part 3

const groceries = { 
	apples: "40", 
	carrots: 10, 
	pears: 20, 
	mushrooms: "100",
	mangos: 5,
	lemons: "5"
}

for(let item in groceries){
    if (typeof groceries[item] === "string"){
        delete groceries[item]
        console.log(`removing ${item}`)
    }
}

//part 4

const employees = { 
    123 : { name: "Worf", age: 61, birthdayMonth: "April 14" },
    124 : { name: "Data", age: 5, birthdayMonth: "March 07" },
    125 : { name: "Geordi", age: 52, birthdayMonth: "June 12" },
    126 : { name: "Seven", age: 32, birthdayMonth: "March 02" },
  }
  
  for(let i in employees) {
    let employee = employees[i]
    if (employee.birthdayMonth.includes("March")){
        employee.age += 1
    }
  }
  console.log(employees)