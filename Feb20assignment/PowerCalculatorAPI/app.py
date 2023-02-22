from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/power', methods=['POST'])
def power():
    if (request.method == 'POST'):
        base = int(request.form['base'])
        power = int(request.form['power'])
        result = f"{str(base)} to the power {str(power)} is {str(base**power)}"
        return render_template('result.html', result=result)


@app.route('/testing', methods=['POST'])
def test():
    if (request.method == 'POST'):
        base = float(request.json['base'])
        power = float(request.json['power'])
        result = f"{str(base)} to the power {str(power)} is {str(base**power)}"
        return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
