import {readFile} from "node:fs";

class KeyDisplay{
    screen: string[][];
    constructor(readonly screenSizeX:number = 50, readonly screenSizeY:number = 6) {
        this.screen = this.createScreen(screenSizeX, screenSizeY);
    }

    rect(x:number, y:number):void {
        for (let X=0; X < x; X++) {
            for (let Y = 0; Y < y; Y++) {
                this.screen[Y][X] = "#"
            }
        }
    }

    private rotateCol(record: number, shift: number): void {
        for (let i = 0; i < shift; i++) {
            const popped: string = this.screen[this.screen.length - 1][record];
            for (let j = this.screen.length - 1; j > 0; j--) {
                this.screen[j][record] = this.screen[j - 1][record];
            }
            this.screen[0][record] = popped;
        }
    }

    private rotateRow(record:number, shift:number): void{
        for (let i = 0; i < shift; i++) {
            const popped: string = this.screen[record].pop();
            this.screen[record].unshift(popped);
        }
    }

    rotate(axis:string, record:number, shift:number): void{
        switch (axis){
            case "row":
                this.rotateRow(record, shift);
                break;

            case "column":
                this.rotateCol(record, shift);
                break;

            default:
                throw new Error(`Unexpected axis: ${axis}`);
        }
    }

    createScreen(screenSizeX:number = 50, screenSizeY:number = 6):string[][] {
        return Array.from({length: screenSizeY}, () => Array(screenSizeX).fill(" "));
    }

    displayScreen():void{
        for (const screenRow of this.screen) {
            const result = [];

            for (let i = 0; i < screenRow.length; i++) {
                result.push(screenRow[i]);

                // After every 5th element, add the item
                if ((i + 1) % 5 === 0) {
                    result.push("\t");
                }
            }
            console.log(result.join(""));
        }
    }

    countOn():number{
        return this.screen.flat().filter(item => item === "#").length;
    }
}

function main(data:string):void {
    let screen = new KeyDisplay();
    for (const line of data.trim().split("\n")) {
        const content = line.trim().split(" ");
         switch(content[0]){
            case "rect":
                const [x, y] = content[1].split("x") as unknown as [number, number];
                screen.rect(x, y);
                break;

            case "rotate":
                const record = content[2].split("=")[1] as unknown as number;
                const shift: number = Number(content[4]);
                screen.rotate(content[1], record, shift);
        }
        screen.displayScreen();
        console.log("________");
    }
    console.log(screen.countOn());
}

readFile("inputs/Day8.txt", "utf8", (err, data) => {
    if (err) throw err;
    main(data)
})
