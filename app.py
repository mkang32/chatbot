from chat.preprocessing import chatbot_response
from flask import Flask, request

app = Flask(__name__)


@app.route('/api/', methods=['POST'])
def get_response():
    data = request.get_data().decode('utf-8')
    res = chatbot_response(data)
    return res


if __name__ == '__main__':
    app.run()
