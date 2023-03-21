def count_delay(a_seconds, c_seconds):
    day_seconds = convert_to_seconds(24, 0, 0)

    if c_seconds >= a_seconds:
        sum_seconds = c_seconds - a_seconds
    else:
        sum_seconds = (day_seconds - a_seconds) + c_seconds

    if sum_seconds % 2 == 0:
        delay_seconds = sum_seconds // 2
    else:
        delay_seconds = sum_seconds // 2 + 1

    return delay_seconds


def convert_to_seconds(hour, minute, second):
    minutes = 60 * hour + minute
    seconds = 60 * minutes + second

    return seconds


def convert_to_hms(seconds):
    # print(f"{seconds = }")

    seconds_in_minute = 60
    seconds_in_hour = seconds_in_minute * 60
    seconds_in_day = seconds_in_hour * 24

    # print(f"{seconds_in_minute = }")
    # print(f"{seconds_in_hour = }")
    # print(f"{seconds_in_day = }\n")

    h, m, s = 0, 0, 0

    d = seconds // seconds_in_day
    if d > 0:
        seconds -= seconds_in_day

    h = seconds // seconds_in_hour
    m = (seconds - (h * seconds_in_hour)) // seconds_in_minute
    s = seconds - (h * seconds_in_hour) - (m * seconds_in_minute)

    hms_string = "{:02d}:{:02d}:{:02d}".format(h, m, s)

    return hms_string


def count_exact_time(a, b, c):
    a_hour, a_minute, a_second = map(int, a.split(":"))
    a_seconds = convert_to_seconds(a_hour, a_minute, a_second)

    c_hour, c_minute, c_second = map(int, c.split(":"))
    c_seconds = convert_to_seconds(c_hour, c_minute, c_second)

    delay_seconds = count_delay(a_seconds, c_seconds)
    # print(f"{delay_seconds = }\n")

    b_hour, b_minute, b_second = map(int, b.split(":"))
    b_seconds = convert_to_seconds(b_hour, b_minute, b_second)

    exact_time = convert_to_hms(b_seconds + delay_seconds)

    return exact_time


if __name__ == "__main__":
    a = input()
    b = input()
    c = input()

    # 18:10:05
    # a = "15:01:00"
    # b = "18:09:45"
    # c = "15:01:40"

    # 06:09:45
    # a = "15:01:00"
    # b = "18:09:45"
    # c = "15:00:59"

    print(count_exact_time(a, b, c))
