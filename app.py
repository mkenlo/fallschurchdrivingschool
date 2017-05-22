from flask import (Flask, render_template,
                   request, url_for)
import requests
import time

app = Flask(__name__)

apiKey = "key-96eec8a34bfab703665c0cb8a4ac9db2"
domain = "https://api.mailgun.net/v3/sandboxa9a2a9803846408fb0b1d907868964d0.mailgun.org/messages"
manager = "fallchurchdriving@hotmail.com"
firstInstructor = "mohfe@hotmail.co.uk"
webmaster = "fallchurchds@gmail.com"


@app.route('/')
def home():
    return render_template('index.html', site_copyright=time.strftime("%Y"))


def send_message(adrTo, subject, message):
    msgFrom = "Falls Church Driving School"
    return requests.post(domain,
                         auth=("api", apiKey),
                         data={"from": msgFrom,
                               "to": adrTo,
                               "subject": subject,
                               "text": message})


@app.route('/mailus', methods=['POST'])
def sendmail():
    if request.method == 'POST':
        message = "Hi, My name is %s." % request.form['customer-name']
        message += "I would like to know more about %s." % request.form[
            'service']
        message += "Contact me at %s." % request.form['customer-phone']
        message += "I live in %s." % request.form['customer-adr']
        message += "This is my plus message: %s" % request.form['message']
        subject = "Hi, you have a new message from %s" % request.form[
            "customer-name"]
        send_message(webmaster, subject, message)
        send_message(manager, subject, message)
        send_message(firstInstructor, subject, message)
    return render_template('mailus.html', site_copyright=time.strftime("%Y"))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
