import * as fs from "fs";


function isValidTriangle(line): boolean {
    // const [a, b, c] = line.trim().split("  ").map(Number);
    const [a, b, c] = line
    if ((a + b > c) && (a + c > b) && (b + c > a)) return true;
}

function getThreeTriangles(data: string): number {
    let count: number = 0;
    const formatted = data.split("\n").map(line => line.trim().split(/\s+/).map(Number));
   for (let i = 0; i < formatted.length - 2; i += 3) {
        const t1 = [formatted[i][0], formatted[i + 1][0], formatted[i + 2][0]];
        const t2 = [formatted[i][1], formatted[i + 1][1], formatted[i + 2][1]];
        const t3 = [formatted[i][2], formatted[i + 1][2], formatted[i + 2][2]];

        if (isValidTriangle(t1)) count++;
        if (isValidTriangle(t2)) count++;
        if (isValidTriangle(t3)) count++;
       console.log(t1, t2, t3)
    }
    return count
}

fs.readFile("inputs/Day3.txt", "utf8", (err, data) => {
    if (err) throw err;
    console.log(getThreeTriangles(data));
});