let cat = Object.create({type:"lion"});
cat.size = "large";

let copyCat = {...cat}
cat.type = "tiger"

console.log(copyCat)