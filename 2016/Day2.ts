import * as fs from "fs"


let keypad: string[][];
// keypad =
// [["1", "2", "3"],
//  ["4", "5", "6"],
//  ["7", "8", "9"]];

keypad = [["Z", "Z", "1", "Z","Z"],
        ["Z","2","3","4","Z"],
        ["5","6","7","8","9"],
        ["Z","A", "B", "C","Z"],
        ["Z","Z","D","Z","Z"]];



function moveCursor(line: string, cursor: number[]): number[] {
    for (const char of line.trim()) {
        let lastCursor: number[] = cursor.slice();
        switch (char) {
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
        if (cursor[0] < 0 || cursor[1] < 0 || cursor[0] > 4 || cursor[1] > 4) {
            cursor = lastCursor;
        }
        if (readCursor(cursor) === "Z") {
            cursor = lastCursor;
        }
    }
    return cursor;
}

function readCursor(cursor: number[]): string{
    return keypad[cursor[1]][cursor[0]];
}


let cursor: number[] = [0, 2];
fs.readFile("inputs/Day2.txt", "utf8", (err, data) => {
    if (err) throw err;
    let code: string = "";
    for (const line of data.split("\n")) {
        cursor = moveCursor(line, cursor)
        code += readCursor(cursor);
}
    console.log(code)}
);