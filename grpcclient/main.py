from flask import Flask, render_template, jsonify, request, url_for, redirect
from proto_class import Client

app = Flask(__name__)

@app.route('/',methods =['POST','GET'])
def hello_world():
    return 'GRPC Demo'

@app.route('/post', methods=["POST"])
def grpc():

    input_json = request.get_json(force=True)
    client = Client()
    name=input_json['Serial']
    response = client.get_response(message=name)
    print(response)
    dictToReturn = {'text': response.serial}

    return jsonify(dictToReturn)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)





