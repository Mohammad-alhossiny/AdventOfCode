import * as fs from "fs";


function isValidTriangle(line: string): boolean {
   const [a, b, c] = line.trim().split("  ").map(Number);
      return (a + b > c) && (a + c > b) && (b + c > a);
}

fs.readFile("inputs/Day3.txt", "utf8", (err, data) => {
    if (err) throw err;
    let count = 0;
    for (let line of data.split("\n")) {
        if (isValidTriangle(line)) {count++}
    }
    console.log(count);
});