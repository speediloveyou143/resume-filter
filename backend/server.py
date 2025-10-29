from flask import Flask,request,jsonify

app=Flask(__name__)

@app.route('/',methods=["GET"])
def home():
    return jsonify({"message":"this is home page"})


app.run(debug=True)