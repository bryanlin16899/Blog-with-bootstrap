from flask import Flask, render_template, request
import requests
import smtplib

my_email = "brian16899@gmail.com"
my_password = "hygnjutbm03"

posts = requests.get(url="https://api.npoint.io/e42b353ee387383898c7").json()

app = Flask(__name__)


@app.route("/")
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def get_about():
    return render_template("about.html")


@app.route("/contact", methods=['POST'])
def get_contact():
    if request.method == 'POST':
        data = request.form
        name = data["name"]
        email = data["email"]
        phone = data["phone"]
        message = data['message']
        send_email(name, email, phone, message)
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    with smtplib.SMTP("smtp.gmail.com") as conncetion:
        conncetion.ehlo()
        conncetion.starttls()
        conncetion.ehlo()
        conncetion.login(user=my_email, password=my_password)
        conncetion.sendmail(from_addr=email, to_addrs=my_email, msg=f"Subject:Website.\n\n"
                                                                    f"Name:{name}\nemail:{email}\nphone:{phone}\n"
                                                                    f"message:{message}.")


@app.route("/<int:index>")
def get_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
