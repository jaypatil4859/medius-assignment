from flask import Flask, render_template
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'ijaypatil04@gmail.com'
app.config['MAIL_PASSWORD'] = 'jcpbqpcepkdbsrps'

mail = Mail(app)

@app.route('/')
def send_email():
    msg = Message(
        subject="Python (Selenium) Assignment - Jay Patil",
        sender=app.config['MAIL_USERNAME'],
        recipients=["tech@themedius.ai"],
        cc=["hr@themedius.ai"]
    )
    msg.body = """ Here are the details for my assignment submission:
        1. Screenshot of the form filled via code:
        2. Source code (GitHub repository): https://github.com/jaypatil4859/medius-assignment
        3. Brief documentation of my approach
        4. My resume
        5. Links to past projects/work samples: https://drive.google.com/drive/folders/1F2GUff0bJ_ig-nMNqRSxSKkg_tLQe0cn?usp=drive_link
        6. Availability confirmation: Yes, I am available full time 10 am to 7 pm for the next 3-6 months.

        Best regards,
        Jay Patil
        """
    

    # Attach files
    with app.open_resource("confirmation_page.png") as fp:
        msg.attach("confirmation_page.png", "image/png", fp.read())
    with app.open_resource("JAY PATIL RESUME.pdf") as fp:
        msg.attach("JAY PATIL RESUME.pdf", "application/pdf", fp.read())
    with app.open_resource("documentation.txt") as fp:
        msg.attach("documentation.txt", "text/plain", fp.read())

    mail.send(msg)
    return "Email sent!"

if __name__ == '__main__':
    app.run(debug=True)
 