def solution(my_string, overwrite_string, s):
    answer = ''
    my = my_string[:s]
    end = my_string[s+len(overwrite_string):]
    answer = my + overwrite_string + end
    return answer