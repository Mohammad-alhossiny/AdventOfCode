# 8 lc letters
# has to have 3 consecetive letters
# can't have  i o l
# two diferent douples

def no_banned_letters(string:str) -> bool:
    return not any(l in string for l in "iol")
    

def three_in_a_row(in_list:list) -> bool:
    for i in range(len(in_list) - 2):
        if (in_list[i] == (in_list[i+1]-1) == (in_list[i+2]-2)):
            return True
    return False

def has_douples(in_list):
    n_ds = 0
    skip_next = False
    
    for i in range(len(in_list) - 1):
        if not skip_next:
            if (in_list[i] == (in_list[i+1])):
                n_ds += 1
                skip_next = True
        else:
            skip_next = False
        if n_ds >= 2:
            return True
    return False

def increment_string(string:str) -> str: 
    string_list = list(string)
    if string_list[-1] == "z":
        string_list.pop()
        new_string = increment_string(string[:-1]) + "a" 
        return new_string
    else:
        ord_list = [ord(i) for i in string_list]
        ord_list[-1] += 1
        char_list = [chr(i) for i in ord_list]
        return "".join(char_list)

        

def certify_str(string:str) -> str:
    if no_banned_letters(string):
        string_ord = [ord(l) for l in string]
        if three_in_a_row(string_ord):
            if has_douples(string_ord):
                return True

def new_pass(string:str):    
    while True:
        string = increment_string(string)
        if string.islower() and len(string) == 8:
            if certify_str(string):
                return string
        else:
            string = "a" * 8
            return new_pass()

string = "hxbxwxba"
if __name__ == "__main__":
    string = new_pass(string)
    print(new_pass(string))