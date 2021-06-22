from chat.preprocessing import chatbot_response
from flask import Flask, redirect, url_for, request
app = Flask(__name__)


@app.route('/response/<sentence>')
def response(sentence):
    res = chatbot_response(sentence)
    return res


@app.route('/chatbox', methods=['POST'])
def chatbox():
    sentence = request.form['nm']
    return redirect(url_for('response', sentence=sentence))


if __name__ == '__main__':
    app.run()
