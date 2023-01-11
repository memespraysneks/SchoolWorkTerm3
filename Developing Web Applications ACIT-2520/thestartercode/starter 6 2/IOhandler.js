/*
 * Project: Milestone 1
 * File Name: IOhandler.js
 * Description: Collection of functions for files input/output related operations
 *
 * Created Date:
 * Author:
 *
 */

const unzipper = require("unzipper"),
  fs = require("fs"),
  PNG = require("pngjs").PNG,
  path = require("path");

/**
 * Description: decompress file from given pathIn, write to given pathOut
 *
 * @param {string} pathIn
 * @param {string} pathOut
 * @return {promise}
 */
const unzip = async (pathIn, pathOut) => {
  let data = fs.createReadStream(pathIn)
  .pipe(unzipper.Extract({ path: pathOut}))
  .promise()
  .then(() => console.log("Unzip Successful"))
  .catch(err=>console.log(err))
  return data
};

/**
 * Description: read all the png files from given directory and return Promise containing array of each png file path
 *
 * @param {string} path
 * @return {promise}
 */
const readDir = (dir) => {
  let data = fs.promises.readdir(dir)
  .then(filenames => {
    let pngPaths = []
    for (let filename of filenames) {
      let ext = path.extname(filename);
      if (ext == "png"){
        pngPaths.push(filename)
      }
    }
  })
};

/**
 * Description: Read in png file by given pathIn,
 * convert to grayscale and write to given pathOut
 *
 * @param {string} filePath
 * @param {string} pathProcessed
 * @return {promise}
 */
const grayScale = (pathIn, pathOut) => {
  return new Promise((resolve, reject) => {
    resolve(
      fs.createReadStream(pathIn)
      .pipe(
        new PNG()
      )
      .on("parsed", function(){
        for (var i = 0; i < this.data.length; i += 4){
          grey = (this.data[i] + this.data[i+1] + this.data[i+2])/3
          this.data[i] = grey
          this.data[i+1] = grey
          this.data[i+2] = grey
        }
        this.pack().pipe(fs.createWriteStream(pathOut))
      })
    )
    reject()
  })
};

module.exports = {
  unzip,
  readDir,
  grayScale,
};
