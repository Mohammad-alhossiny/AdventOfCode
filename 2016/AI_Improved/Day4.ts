// Represents the data structure for room information after parsing
import {readFile} from "node:fs";

interface RoomParts {
    name: string;           // Raw name containing hyphens
    id: number;            // Room sector ID
    checksum: string;      // Expected checksum value
}

// Represents processed room data ready for validation
interface ProcessedRoom extends RoomParts {
    cleanName: string;     // Name with only lowercase letters
    decryptedName: string; // Name after shift cipher decryption
}

// Represents character frequency count
interface CharCount {
    [char: string]: number;
}

// Configuration for the cipher algorithm
interface CipherConfig {
    startCode: number;     // ASCII code for 'a'
    alphabetSize: number;  // Size of the alphabet (26)
}

// Results of room processing
interface RoomProcessingResults {
    idSum: number;         // Sum of valid room IDs
    validRooms: ProcessedRoom[];  // Array of valid rooms
    invalidRooms: RoomParts[];    // Array of invalid rooms
}

// Error types for better error handling
interface RoomError extends Error {
    type: 'PARSE_ERROR' | 'VALIDATION_ERROR' | 'DECRYPT_ERROR';
    roomData?: string;
}

const CIPHER_CONFIG: CipherConfig = {
    startCode: 'a'.charCodeAt(0),
    alphabetSize: 26
};

function createRoomError(message: string, type: RoomError['type'], roomData?: string): RoomError {
    const error = new Error(message) as RoomError;
    error.type = type;
    error.roomData = roomData;
    return error;
}

function parseRoomParts(line: string): RoomParts {
    const match = line.trim().match(/^(.*)-(\d+)\[([a-z]+)\]$/);
    if (!match) {
        throw createRoomError(
            `Invalid room format: ${line}`,
            'PARSE_ERROR',
            line
        );
    }

    const [, name, idStr, checksum] = match;
    if (checksum.length !== 5) {
        throw createRoomError(
            `Invalid checksum length: ${checksum}`,
            'VALIDATION_ERROR',
            line
        );
    }

    return {
        name,
        id: Number(idStr),
        checksum
    };
}

function processRoom(parts: RoomParts): ProcessedRoom {
    const cleanName = parts.name.replace(/[^a-z]/g, "");
    const decryptedName = decryptRoomName(parts.name, parts.id);

    return {
        ...parts,
        cleanName,
        decryptedName
    };
}

function countChars(name: string): CharCount {
    return name.split("").reduce((counts, char) => {
        if (/[a-z]/.test(char)) {
            counts[char] = (counts[char] || 0) + 1;
        }
        return counts;
    }, {} as CharCount);
}

function calculateChecksum(charCounts: CharCount): string {
    return Object.entries(charCounts)
        .sort(([charA, countA], [charB, countB]) => {
            if (countA === countB) {
                return charA.localeCompare(charB);
            }
            return countB - countA;
        })
        .map(([char]) => char)
        .slice(0, 5)
        .join("");
}

function isValidRoom(room: ProcessedRoom): boolean {
    const charCounts = countChars(room.cleanName);
    const calculatedChecksum = calculateChecksum(charCounts);
    return calculatedChecksum === room.checksum;
}

function decryptRoomName(name: string, id: number): string {
    return name
        .split("")
        .map(char => {
            if (char === "-" || char === ",") return " ";
            if (!/[a-z]/.test(char)) return char;

            const charCode = char.charCodeAt(0);
            const shifted = (
                (charCode - CIPHER_CONFIG.startCode + id)
                % CIPHER_CONFIG.alphabetSize
            ) + CIPHER_CONFIG.startCode;

            return String.fromCharCode(shifted);
        })
        .join("");
}

function processRooms(data: string): RoomProcessingResults {
    const lines = data.trim().split("\n");
    const results: RoomProcessingResults = {
        idSum: 0,
        validRooms: [],
        invalidRooms: []
    };

    for (const line of lines) {
        try {
            const parts = parseRoomParts(line);
            const processedRoom = processRoom(parts);

            if (isValidRoom(processedRoom)) {
                results.idSum += processedRoom.id;
                results.validRooms.push(processedRoom);

                if (processedRoom.decryptedName.includes("north")) {
                    console.log(`Found north-related room:`, {
                        id: processedRoom.id,
                        decrypted: processedRoom.decryptedName
                    });
                }
            } else {
                results.invalidRooms.push(parts);
            }
        } catch (error) {
            console.error(`Error processing line: ${line}`, error);
            continue;
        }
    }

    return results;
}

// Read and process the file
readFile("../inputs/Day4.txt", "utf8", (err, data) => {
    if (err) {
        console.error("Error reading file:", err);
        process.exit(1);
    }

    try {
        const results = processRooms(data);
        console.log(`Summary:
            Valid Rooms: ${results.validRooms.length}
            Invalid Rooms: ${results.invalidRooms.length}
            Sum of Valid IDs: ${results.idSum}
        `);
    } catch (error) {
        console.error("Error processing rooms:", error);
        process.exit(1);
    }
});