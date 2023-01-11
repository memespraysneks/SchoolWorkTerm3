const path = require("path");
/*
 * Project: Milestone 1
 * File Name: main.js
 * Description:
 *
 * Created Date:
 * Author:
 *
 */

const IOhandler = require("./IOhandler");
const zipFilePath = path.join(__dirname, "myfile.zip");
const pathUnzipped = path.join(__dirname, "unzipped");
const pathProcessed = path.join(__dirname, "grayscaled");

IOhandler.unzip(zipFilePath, pathUnzipped)
.then(() => IOhandler.readDir(pathUnzipped))
.then((unzipped) => {
    for (image of unzipped) {
        let pathIn = pathUnzipped + "/" + image
        let pathOut = pathProcessed + "/" + image
        IOhandler.grayScale(pathIn, pathOut)
    }
})
.catch((err) => console.log(err))