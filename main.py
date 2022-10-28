from flask import Flask, render_template, request, werkzeug, flash

app = Flask(__name__)
app.secret_key = "secret_key_for_escaping_problems"
coordinate = 3 # var. che conterrà le coordinate elaborate dal modello di matteo

#selecting a route for our app
@app.route("/hello") #/hello will represent the last part of our URL
def index(): #verrà eseguita quando verrà messo l'URL finale con /hello
    flash("what's your name?")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"]) #specifico i metodi che voglio perchè sto interagendo con il server
def greet():
    flash("Hi " + str(request.form['name_input']) + ", great to see you!")
    return render_template("index.html")

#POST: per mandare l'immagine al server per essere elaborata
@app.route('/dataexchange',methods = ['POST'])
def dataexchange():
   if request.method == 'POST':
       imagefile = Flask.request.files['image']
       filename = werkzeug.utils.secure_filename(imagefile.filename)
       print("\nReceived image File name : " + imagefile.filename)
       imagefile.save(filename)
       print("Image Uploaded Successfully. Please wait: your image is been processed...")
       return coordinate


if __name__ == '__main__':
    app.run(debug=True)