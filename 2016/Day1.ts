import * as fs from "fs";

const location = {
    x: 0,
    y: 0,
    facing: "North",
    visited: new Set("0, 0"),
    absDist(): number {
        return Math.abs(this.x) + Math.abs(this.y);
    },
    move(input: string): void{
        let direction: string = input.charAt(0); // L or R
        let scale: number = Number(input.slice(1)); // Distance
        // Update facing direction first
        if (direction === "L") {
            switch (this.facing) {
                case "North":
                    this.facing = "West";
                    break;
                case "South":
                    this.facing = "East";
                    break;
                case "East":
                    this.facing = "North";
                    break;
                case "West":
                    this.facing = "South";
                    break;
            }
        } else if (direction === "R") {
            switch (this.facing) {
                case "North":
                    this.facing = "East";
                    break;
                case "South":
                    this.facing = "West";
                    break;
                case "East":
                    this.facing = "South";
                    break;
                case "West":
                    this.facing = "North";
                    break;
            }
        }
        // Move in the new facing direction
        const prevLocX: number = this.x;
        const prevLocY: number = this.y;
        switch (this.facing) {
            case "North":
                this.y += scale;
                this.addVisitedRange(this.x, this.y, prevLocY, "y")
                break;  // Moving North increases y
            case "South":
                this.y -= scale;
                this.addVisitedRange(this.x, this.y, prevLocY, "y")
                break;  // Moving South decreases y
            case "East":
                this.x += scale;
                this.addVisitedRange(this.x, this.y, prevLocX, "x")
                break;   // Moving East increases x
            case "West":
                this.x -= scale;
                this.addVisitedRange(this.x, this.y, prevLocX, "x")
                break;   // Moving West decreases x
        }
    },
    addVisitedRange(newX:number, newY:number, prev:number, modifiedAxis:string): void{
        switch (modifiedAxis){
            case "y":
                const startY = Math.min(prev, newY);
                const endY = Math.max(prev, newY);
                for (let i = startY; i <= endY; i++) {
                    if (this.visited.has(`${newX}, ${i}`) && i !== prev){
                        console.log(`${newX}, ${i} distance: `, (Math.abs(newX) + Math.abs(i)))
                    } else {
                        this.visited.add(`${newX}, ${i}`);
                    }
                }
                break;

            case "x":
                const startX = Math.min(prev, newX);
                const endX = Math.max(prev, newX);
                for (let i = startX; i <= endX; i++) {
                    if (this.visited.has(`${i}, ${newY}`) && i !== prev){
                       console.log(`${i}, ${newY} distance:`, (Math.abs(newY) + Math.abs(i)))
                    }else {
                        this.visited.add(`${i}, ${newY}`)
                    }
                }
                break
        }
    }
}
fs.readFile("inputs/Day1.txt", "utf8", (err, data) => {
    if (err) throw err;
    for (let command of data.split(",")) {
        command = command.trim()
        location.move(command);
    }
});
// const data: string = "R8, R4, R4, R8"
// for (let command of data.split(",")) {
//     command = command.trim()
//     // console.log(command, location.x, location.y, location.facing);
//     location.move(command);
//     // console.log(location.x, location.y);
// }