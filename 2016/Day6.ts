import {readFile} from "node:fs";


function parseLines(input: string) {
    const lines: string[] = input.trim().split("\n").map((line) => line.trim());
    let letters: string[][] = Array.from({length: lines[0].length}, () => []);
    for (const line of lines) {
        for (let i = 0; i < lines[0].length; i++) {
            letters[i].push(line[i])
        }
    }
    return letters;
}

function mostRepeated(letter: string[]): string {
   let counts: {[char: string]: number} = {}; let result:string;
    for (const c of letter) {
        counts[c] = (counts[c] || 0) + 1;
    }
    result = Object.entries(counts).sort(([, a], [, b])=> b-a)[0][0];
    return result;
}


function main(input: string): string {
    let message: string = "";
    const letters: string[][] = parseLines(input);
    for (const letterList of letters) {
        const char = mostRepeated(letterList);
        message += char;
    }
    console.log(message);
    return message;
}

// const data: string = "eedadn\n" +
//     "drvtee\n" +
//     "eandsr\n" +
//     "raavrd\n" +
//     "atevrs\n" +
//     "tsrnev\n" +
//     "sdttsa\n" +
//     "rasrtv\n" +
//     "nssdts\n" +
//     "ntnada\n" +
//     "svetve\n" +
//     "tesnvt\n" +
//     "vntsnd\n" +
//     "vrdear\n" +
//     "dvrsen\n" +
//     "enarar";
//
// main(data)
readFile("inputs/Day6.txt", "utf8", (err, data) => {
    if (err) throw err;
    main(data);
})
