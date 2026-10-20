import jdatetime

def to_jalali(value, fmt="%Y/%m/%d"):
    if not value:
        return ""
    return jdatetime.date.fromgregorian(date=value).strftime(fmt)