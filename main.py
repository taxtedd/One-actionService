from flask import Flask, request, render_template


def toweb(f):
    app = Flask(__name__)

    @app.route("/", methods=['GET', 'POST'])
    def first_page():
        a = f.__annotations__
        if 'return' in a:
            a.pop('return')

        if request.form:
            res = f(**request.form)
        else:
            res = None
        titles = {'num': 'Число', 'fromSys': 'Исходная С. С.', 'intoSys': 'Новая С. С.'}
        return render_template('first_page.html', about="Замена системы счисления", a=a, res=res, titles=titles)

    return app


def maxNum(num):
    mx = 0
    for el in num:
        mx = max(mx, int(el))
    return mx


@toweb
def s(num: str, fromSys: str, intoSys: str) -> int:
    fromSys, intoSys = int(fromSys), int(intoSys)
    if fromSys > 16 or intoSys > 16 or maxNum(num) >= fromSys:
        return "некорректные входные данные!"
    num = int(num, fromSys)
    res = ''
    s = '01234567889ABCDEF'
    while num > 0:
        res = s[num % intoSys] + res
        num //= intoSys
    return res


s.run(host='0.0.0.0', port="5001")
