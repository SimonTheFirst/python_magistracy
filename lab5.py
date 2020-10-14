from datetime import datetime

def sort_dates(lst, mode):
    pattern = "%d-%m-%Y_%H:%M"
    date_lst = [datetime.strptime(x, pattern) for x in lst]
    if mode == "ASC":
        date_lst.sort()
    else:
        date_lst.sort(reverse=True)
    return [x.strftime(pattern) for x in date_lst]

if __name__ == "__main__":
    print(sort_dates(["10-02-2018_12:30", "10-02-2016_12:30", "10-02-2018_12:15"], "ASC") )
    print(sort_dates(["10-02-2018_12:30", "10-02-2016_12:30", "10-02-2018_12:15"], "DSC") )
    print(sort_dates(["09-02-2000_10:03", "10-02-2000_18:29", "01-01-1999_00:55"], "ASC") )