const unzip = (pathIn, pathOut) => {
    return new Promise((resolve, reject) => {
        fs.createReadStream("path/to/archive")
        .pipe(unzipper.Extract({path: "output/path"}))
        .on("error", (err) => reject(err))
    })
}
