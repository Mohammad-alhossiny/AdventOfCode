// @ts-ignore
import fs from "fs";

function returnParts(line: string): [string, number, string] {
    let name:string; let id:number; let checksum:string;
    let arr:string[] = line.split('-');
    name = arr.slice(0, arr.length - 1).toString();
    id = Number(arr[arr.length - 1].split("[")[0]);
    checksum = arr[arr.length - 1].split("[")[1];
    checksum = checksum.replace("]", "");

    return [name, id, checksum];
}

function countChars(name: string): {[char: string]: number} {
    const counts: {[char: string]: number} = {};
    for (const char of name) {
        counts[char] = (counts[char] || 0) +  1;
    }
    return counts;
}

function getChecksum(countChars: object, checksum:string): boolean {
    let strCalcChecksum: string;
    let calcChecksum:[string, number][]= Object.entries(countChars).sort(([ka, a], [kb, b]) => {
        if (a === b){
            return ka.localeCompare(kb);
        }
        return b - a;
    })
    strCalcChecksum = calcChecksum.map(pair => pair[0]).join("").slice(0,5)
    return strCalcChecksum.trim() === checksum.trim();
}

function decrypt(name:string, id:number): string {
    const startCode = "a".charCodeAt(0);
    let decrypted:string = "";
    for (const char of name) {
        if (char == ","){
            decrypted = decrypted.concat(" ")
        } else{
            const charCode: number = char.charCodeAt(0);
            const decryptedChar: string = String.fromCharCode(((charCode - startCode + id) % 26) + startCode);
            decrypted = decrypted.concat(decryptedChar)
        }
    }
    return decrypted;
}

function main(data:string):number {
    let countValids: number = 0; let idSum:number =0; let validRooms:string[] = [];

    for (const line of data.split("\n")){
        let nameUnmodded:string; let id:number; let checksum:string; let name:string;
        [nameUnmodded, id, checksum] = returnParts(line);
        name = nameUnmodded.replace(/[^a-z]/g, "");
        if (getChecksum(countChars(name), checksum)){
            countValids++;
            idSum += id;
            let decrypted: string = decrypt(nameUnmodded, id)
            validRooms.push(decrypted);
            if (decrypted.includes("north")){
                console.log(id);
            }

        }
    }
    return idSum;
}


fs.readFile("inputs/Day4.txt", "utf8", (err, data) => {
    if (err) throw err;
    main(data)
});