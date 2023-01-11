const wordPosition = (words) => {
    const dict = {}
    const temp = [...words]
    const set = new Set(temp.sort())
    const indvWords = Array.from(set)
    for (let word = 0; word < indvWords.length; word++){
        let currentWord = indvWords[word]
        dict[currentWord] = []
    }
    for (let word = 0; word < words.length; word++){
        let currentWord = words[word]
        dict[currentWord].push(word)        
    }
    return dict
}
    
const input = [
    "buy",
    "it",
    "use",
    "it",
    "break",
    "it",
    "fix",
    "it",
    "trash",
    "it",
    "change",
    "it",
    "mail",
    "upgrade",
    "it",
];



const output = wordPosition(input);
 
console.log(output)
    /*
    Output should look like so:
    {
      break: [ 4 ],
      buy: [ 0 ],
      change: [10],
      fix: [ 6 ],
      it:  [1, 3, 5, 7, 9, 11, 14],
      mail: [ 12 ],
      trash: [ 8 ],
      upgrade: [ 13 ],
      use: [ 2 ],
    }
    
    */