fs = require("fs")
const {filteringFunc} = require("./module")

const extensionFinder = (dir, extension) => {
    filteringFunc(dir, extension, (err, files) => {
			if(err){
				console.log(err)
			}
			for (file of files){
				console.log(file)
			}
		}
    )
}

extensionFinder("./", ".js")