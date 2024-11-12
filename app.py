from flask import Flask
import os
import time
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Siddhardh Muthoja"  
    username = os.getenv('USER') or os.getenv('USERNAME') or "unknown"
    server_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    top_output = subprocess.getoutput('top -bn1 | head -n 20')

    html_content = f"""
    <h2>Server Info</h2>
    <p><b>Name:</b> {name}</p>
    <p><b>Username:</b> {username}</p>
    <p><b>Server Time (IST):</b> {server_time}</p>
    <pre>{top_output}</pre>
    """

    return html_content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

