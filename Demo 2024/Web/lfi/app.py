from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    path = 'story.txt' # default
    if request.args.get('file') is not None and os.path.exists(request.args.get('file')):
        path = request.args.get('file')
    else:
        return render_template('home.html', file = 'Enggak ada :(')
    fd = os.open(path, os.O_RDONLY)
    read = os.read(fd, 4096)
    data = read

    return render_template('home.html', file = data.decode())

@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, PermissionError):
        return '<img src="https://media.discordapp.net/attachments/1186104586914779266/1274005706214735892/nakal.gif?ex=66c0adc6&is=66bf5c46&hm=3ca872ac74f171cf4f2029e47a7c0c1c80946a6088674b8a6489a92c471e3a40&=&width=365&height=188">'

app.run(host='0.0.0.0', port=2567)