
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        return "Image received successfully!"
    return '''
        <h2>AI Image Detector</h2>
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="image">
            <input type="submit">
        </form>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
