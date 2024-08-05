def date_format(date_str):
    parts = date_str.split('/')

    month = parts[0]
    day = parts[1]
    year = parts[2]

    return f"{year}-{month.zfill(2)}-{day.zfill(2)}"
