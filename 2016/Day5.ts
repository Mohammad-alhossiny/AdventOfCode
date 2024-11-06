import {md5} from "js-md5";

let code:string =""; const start:string="ojvtpuvg"; let count:number = 0;

while (true){
    const iter: string = start.concat(String(count));
    md5(iter);
    let coded = String(md5.create().update(iter).hex());
    if(coded.slice(0, 5) === "00000"){
        code = code.concat(coded[5]);
        if (code.length == 8){
            console.log(code);
            break;
        }
    }
    if (count % 1000 === 0){
        console.log(code, "1000 tries");
    }
    count++;
}