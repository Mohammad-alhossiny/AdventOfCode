import {md5} from "js-md5";

let code:object ={};
const start:string="ojvtpuvg"; let count:number = 0;
// const start:string="abc"; let count:number = 3231929;

while (true){
    const iter: string = start.concat(String(count));
    md5(iter);
    let coded = String(md5.create().update(iter).hex());
    let tupes: [string, string][];
    if(coded.slice(0, 5) === "00000") {
        try {
            if (code[coded[5]] === undefined){code[coded[5]] = coded[6];}
            tupes = Object.entries(code).sort(([a,], [b,]) => Number(a) - Number(b));
            let output: string = "";
            for (const char of tupes) {
                if (Number(char[0]) < 8) {
                    output += char[1];
                }
            }
            if (output.length === 8) {
                console.log(output);
                break;
            }
        } catch(err) {
            continue;
        }
    }
    if (count % 1000 === 0){
        console.log(code, "1000 tries");
    }
    count++;
}