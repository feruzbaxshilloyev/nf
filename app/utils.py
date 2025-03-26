import requests


def bank():
    url = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
    r = requests.get(url).json()
    r_r = {}
    for i in r:
        if i["Ccy"] == "USD":
            r_r.update({"USD": float(i["Rate"])})
            break
    for i in r:
        if i["Ccy"] == "EUR":
            r_r.update({"EUR": float(i["Rate"])})
            break
    for i in r:
        if i["Ccy"] == "RUB":
            r_r.update({"RUB": float(i["Rate"])})
            break
    return r_r
