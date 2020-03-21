var readline = require('readline');
var rl = readline.createInterface({
  input: process.stdin
});

var lines = []

rl.on('line', function (line) {
    lines.push(line)
});

rl.on('close', function() {
    solve(lines)
})

//拿到所有資料
function solve(lines) {
  var line = lines[0] //1,2
  var temp = line.split(' ') //['1','2']
  console.log(Number(temp[0]) + Number(temp[1]))
}

//1 1
//2 3
//0 0
