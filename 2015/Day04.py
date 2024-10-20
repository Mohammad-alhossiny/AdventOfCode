import hashlib


input_string = "yzbqklnj"
i = 0


while True:
    new_string = input_string + str(i)
    hashed = (hashlib.md5(new_string.encode())).hexdigest()

    if str(hashed)[0:6] == "000000":
        print(hashed ,"\n", i)
        break

    if i%1000 == 0:
        print(f"completed {i} iterations")
    i += 1