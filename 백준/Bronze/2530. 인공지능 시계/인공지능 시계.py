now_time = list(map(int, input().split()))
need_time = int(input())

now_time_second = (now_time[0]*60*60) + (now_time[1]*60) + now_time[2]
cooked_time = now_time_second + need_time

cooked_time_second = cooked_time % 60
cooked_time_minute = (cooked_time // 60) % 60
cooked_time_hour = (cooked_time // 60 // 60) % 24



print(cooked_time_hour, cooked_time_minute, cooked_time_second)