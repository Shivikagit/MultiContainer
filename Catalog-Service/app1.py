from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():   
    html = "<h3>Hello APP1{name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" 
    return html.format(name=os.getenv("NAME", "APP1 - world"), hostname=socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)