from flask import Flask, render_template, request
from math import floor

app = Flask(__name__)


hex_num = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15
}

hex_abc = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F"
}
def num_ten(value, base):
    value = str(value).upper()
    result_10 = 0

    for ch in value:
        digit = hex_num[ch]
        result_10 = result_10 * base + digit

    return result_10



def ten_two(result_10):
    result_2 = ""

    while result_10 > 0:
        num = result_10 % 2
        result_2 = str(num) + result_2
        result_10 //= 2

    return result_2 or "0"

def ten_eight(result_10):
    result_8 = ""

    while result_10 > 0:
        num = result_10 % 8
        result_8 = str(num) + result_8
        result_10 //= 8

    return result_8 or "0"


def ten_sixteen(result_10):
    result_16 = ""

    while result_10 > 0:
        num = result_10 % 16
        if num > 9:
            result_16 = hex_abc[num] + result_16
        else:
            result_16 = str(num) + result_16
        result_10 //= 16

    return result_16 or "0"
        

def convert_all(value, base):
    dec = num_ten(value, base)
    return {
        "bin": ten_two(dec),
        "oct": ten_eight(dec),
        "dec": dec,
        "hex": ten_sixteen(dec)
    }






@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    value = ""
    base = 10

    if request.method == "POST":
        value = request.form.get("value", "").strip()
        base = int(request.form.get("base", 10))

        try:
            result = convert_all(value, base)
        except Exception as e:
            error = str(e)

    return render_template("index.html", result=result, value=value, base=base, error=error)

app.run(debug=True)
