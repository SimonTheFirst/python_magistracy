import datetime as d


def time_adjust(time: str, d_hour: int, d_minute: int, d_second: int):
    pattern = "%H:%M:%S"
    new_time = d.datetime.strptime(time, pattern) + d.timedelta(seconds=d_second, minutes=d_minute, hours=d_hour)
    return d.datetime.strftime(new_time, pattern)


if __name__ == "__main__":
    print(time_adjust("01:00:00", 1, 30, 10))
    print(time_adjust("18:22:30", 4, 60, 30))
    print(time_adjust("00:00:00", 72, 120, 120))


