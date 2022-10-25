from flask import *

app = Flask(__name__)


def Count(num, fromSys, intoSys):
    num = int(num, fromSys)
    res = ''
    s = '01234567889ABCDEF'
    while num > 0:
        res = s[num % intoSys] + res
        num //= intoSys
    return res[::-1]


@app.route('/', methods=['GET', 'POST'])
def first_page():
    answer = ""
    resp = make_response(render_template("first_page.html"))
    if request.method == 'POST':
        num = request.form.get('number')
        fromSys = request.form.get('oldsystem')
        intoSys = request.form.get('newsystem')
        if num != '' and fromSys != '' and intoSys != '':
            answer = Count(num, int(fromSys), int(intoSys))
            print(num)
        return render_template("first_page.html", number=num, oldSystem=fromSys, newSystem=intoSys, answer=answer)
    return render_template("first_page.html")

if __name__ == '__main__':
    app.run(debug=True)
