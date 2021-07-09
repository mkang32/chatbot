from chat.preprocessing import chatbot_response
from flask import Flask, request, make_response, render_template
import os

app = Flask(__name__)

# @app.route('/')
# def home():
#     data = {'url': 'http://127.0.0.1:5000/api/'}
#     return render_template('home.html', data=data)

@app.route('/')
def home():
    return render_template('test.html')

@app.route('/api/', methods=['POST'])
def get_response():
    data = request.get_data().decode('utf-8')
    res = chatbot_response(data)
    res = make_response(res)
    res.mimetype = "text/plain"
    print("This is response:")
    print(res)
    return res


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
