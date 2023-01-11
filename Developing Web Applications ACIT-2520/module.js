const { builtinModules } = require('module')

//module file
fs = require('fs')
path = require('path')

const filteringFunc = (dir, extension, callback) => {
    let files = []                                                                    
    if (typeof dir != 'string') {                                                           
        callback(new Error("Directory or extention is not a string!"), null)                            
		}
    fs.readdir(dir, (err, fileList) => {                                                   
        if (err) {                                                                         
            callback(new Error('List does not exist!'), null)                              
        }
        for (file of fileList) {                                                            
            if (path.extname(file) == extension) {                                               
                files.push(file)                                                    
            }
        }
    callback(null, files)                                                            
    })
}

module.exports = {filteringFunc}