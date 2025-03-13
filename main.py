from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get(url="https://api.npoint.io/faf0d28f6175949280b5")
    all_posts = response.json()
    # return render_template("blog.html", posts=all_posts)
    return render_template("index.html", posts=all_posts)

@app.route("/post/<int:item_id>")
def get_post(item_id):
    response = requests.get(url="https://api.npoint.io/faf0d28f6175949280b5")
    post_num = next(post for post in response.json() if post["id"] == item_id)

    return render_template("post.html", post=post_num)

git remote add origin https://github.com/dlopezkluever/simple-blog
if __name__ == "__main__":
    app.run(debug=True)
