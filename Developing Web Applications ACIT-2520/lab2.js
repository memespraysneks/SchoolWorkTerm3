const mathHelper = require("./mathHelpers");   
const fs = require("fs");                
userNums = process.argv.slice(2)                      



const processInput = (points) => {
    fs.mkdir('./dataPoints', (err) => {                                                 
      if (err) {
        return console.log(err);                                                        
      } 
      else {
        const distance = mathHelper.distance(points[0], points[1], points[2], points[3]); 
        const text = "\nThe distance between your two points: ("+ points[2] + "," + points[0] + "), (" + points[3] + "," + points[1] + ") is " + distance
        fs.writeFile('./dataPoints/points.txt', points.toString(), (err) => {           
          if (err) {
            console.log('Content failed to save')
            return console.log(err);                                                    
          } 
          else {
            console.log('Content saved');                                               
            fs.appendFile('./dataPoints/points.txt', text, (err) => {              
              if (err) {
                return console.log(err);                                                
              }
            });
          }
        });
      }
    });
  };


processInput(userNums)