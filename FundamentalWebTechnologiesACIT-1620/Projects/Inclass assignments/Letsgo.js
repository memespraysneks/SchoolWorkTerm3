const myTodoList = [
    { item: "buy milk", status: "complete" },
    { item: "1620 readings", status: "incomplete" },
    { item: "1620 organize notes", status: "incomplete" },
    { item: "do morning stretches", status: "incomplete" }
  ]

function find_incomplete (){
    let list = []
    for (let item in myTodoList) {
        if (myTodoList[item].status == "incomplete"){
            list.push(myTodoList[item].item)
        }
    }
    console.log(list)
}

find_incomplete()