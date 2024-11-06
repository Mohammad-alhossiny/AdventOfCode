import {readFile} from "node:fs";


function isABBA(sequence:string):boolean {
    for (let i = 0; i < sequence.length -3; i++) {
        const seqOf4: string = sequence.slice(i, i+4);
        if (seqOf4[0] === seqOf4[3] && seqOf4[1] === seqOf4[2] && seqOf4[0] !== seqOf4[1]) {
            return true;
        }
    }
    return false;
}

function matchPattern(seqOf3:string):string[]|boolean {
    if (seqOf3[0] === seqOf3[2] && seqOf3[1] !== seqOf3[0]) {
        const a = seqOf3[0]; const b = seqOf3[1];
        return [a, b];
    }
    return false
}

function isABA(sup:string, hyper:string):boolean {
    for (let i = 0; i < sup.length -2; i++) {
        const seqOf3: string = sup.slice(i, i + 3);
        const aba = matchPattern(seqOf3)
        if (aba) {
            const a = aba[0];
            const b = aba[1];
            if (hyper.includes(b + a + b)) {
                return true;
            }
        }
    }
    return false;
}

function splitHyper(input:string): string[][]{
    let ip: string[] = []; let hyper: string[] = [];
    const line: string[] = input.trim().split(/[\[\]]/g);
    for (let i = 0; i < line.length; i++) {
        switch (i%2){
            case 0:
                ip.push(line[i]);
                break;

            case 1:
                hyper.push(line[i]);
                break
        }
    }
    return [ip, hyper];
}

function countTLS(data:string): number{
    let count: number = 0;
    for (const line of data.trim().split("\n")) {
        const chunks: string[][] = splitHyper(line)??[["not"],["null"]];
        if (chunks[0].some(chunk => isABBA(chunk)) && chunks[1].every(chunk => !isABBA(chunk))) {
            count++;
        }
    }
    return count;
}

function countSSL(data:string): number{
    let count: number = 0;
    for (const line of data.trim().split("\n")) {
        const [sup, hyper]: string[][] = splitHyper(line);
        const supString:string = sup.join("");const hyperString:string = hyper.join("")
        if (isABA(supString, hyperString)){
            count++;
        }
    }
    return count;
}

const test: string = "abba[mnop]qrst\n" +
    "abcd[bddb]xyyx\n" +
    "aaaa[qwer]tyui\n" +
    "ioxxoj[asdfgh]zxcvbn\n"

const test2: string = "aba[bab]xyz\nxyx[xyx]xyx\naaa[kek]eke\nzazbz[bzb]cdb"


console.log(countTLS(test))
console.log(countSSL(test2))

readFile("inputs/Day7.txt", "utf8", (err, data) => {
    if (err) throw err;
    console.log(countTLS(data));
    console.log(countSSL(data));
});
