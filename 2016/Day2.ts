import * as fs from "fs"


let keypad: string[][] =
[["1", "2", "3"],
 ["4", "5", "6"],
 ["7", "8", "9"]];

let cursor: number[] = [1, 1];

function moveCursor(line: string, cursor: number[]): number[] {
    for (const char of line.trim()) {
        let lastCursor: number[] = cursor.slice();
        switch (char){
            case "R":
                cursor[0]++;
                break;
            case "L":
                cursor[0]--;
                break;
            case "U":
                cursor[1]--;
                break;
            case "D":
                cursor[1]++;
                break;
        }
        if (cursor[0] < 0 || cursor[1] < 0 || cursor[0] > 2 || cursor[1] > 2) {
            cursor = lastCursor;
        }
    }
    return cursor;
}

function readCursor(cursor: number[]): string{
    return keypad[cursor[1]][cursor[0]];
}

// const data: string= `ULL
// RRDDD
// LURDL
// UUUUD`;


fs.readFile("inputs/Day2.txt", "utf8", (err, data) => {
    if (err) throw err;
let code: string = "";
for (const line of data.split("\n")) {
    cursor = moveCursor(line, cursor)
    code += readCursor(cursor);
}
console.log(code)
});
