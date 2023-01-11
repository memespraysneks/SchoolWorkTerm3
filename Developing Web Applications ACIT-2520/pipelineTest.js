const fs = require("fs");
const { pipeline, Transform } = require("stream");
const ndjson = require("ndjson");
const positivityJson = require("./afinn.json");
const sort = require("sort-stream2")

const rs = fs.createReadStream("sample.ndjson")

const filterSpam = new Transform({
    objectMode: true,
    transform: function(chunk, enc, push){
        if(chunk.class == 0){
            push(null, chunk)
        } else {
            push(null)
        }
    }
})

let writeStream = fs.createWriteStream('filteredData.ndjson');



const positivityScore = new Transform({
    objectMode: true,
    transform: function(chunk, enc, push){
        chunk.positivityScore = 0
        chunk.reviewText.split(" ").forEach(element => {
            chunk.positivityScore += parseInt(positivityJson[element])
        });
        push(null, JSON.stringify(chunk))
    }
    
})

// .on("data", function (data) {
//     console.log(data)
// })

pipeline(
    rs,
    ndjson.parse(),
    filterSpam,
    positivityScore,
    sort(function(a, b){ return JSON.parse(a).positivityScore - JSON.parse(b).positivityScore }),
    writeStream,
    function (err) {
        if (err){
            console.log(err)
        }
    }
)

