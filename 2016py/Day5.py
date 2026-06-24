import hashlib

def main(inp:str):
    counter = 0
    password = ""
    while True:
        hash_str = inp + str(counter)
        hashed = hashlib.md5(hash_str.encode()).hexdigest()

        if hashed[:5] == "00000":
            password += hashed[5]
            print(password)

        if len(password) == 8:
            break
        counter += 1


def main2(inp:str):
    counter = 0
    password = [None for i in range(8)]
    while True:
        hash_str = inp + str(counter)
        hashed = hashlib.md5(hash_str.encode()).hexdigest()
        position = hashed[5]
        if position.isdigit() and int(position)<8:
            position = int(position)
            if hashed[:5] == "00000" and password[position] is None:
                password[position] = hashed[6]
                print(password)

        if None not in password:
            print("".join(password))
            break
        counter += 1

if __name__ == '__main__':
    test_input:str = "abc"
    actual_input:str = "ojvtpuvg"

    main2(actual_input)

