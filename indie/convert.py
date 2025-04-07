def main():
    ...

def convert(au):
    if not isinstance(au, (int, float)):
        raise TypeError("au must be int or float")
    return au * 149597870700