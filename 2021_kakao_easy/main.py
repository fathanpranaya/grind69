


def solution(s):
    number_dict = {
        "zero"  : "0",
        "one"   : "1",
        "two"   : "2",
        "three" : "3",
        "four"  : "4",
        "five"  : "5",
        "six"   : "6",
        "seven" : "7",
        "eight" : "8",
        "nine"  : "9"
    }
    len_s = len(s)
    temp_number_str = ""
    answer = ""
    for i in range(len_s):
        # check if the current character is alphabetical
        if s[i] in number_dict.values():
            answer += s[i]
        else:
            temp_number_str += s[i]
            if number_dict.get(temp_number_str) is not None:
                answer += number_dict[temp_number_str]
                temp_number_str = ""
        
    return int(answer)

if __name__ == "__main__":
    print(solution("one4seveneight"))