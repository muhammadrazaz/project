from flask import Flask,render_template

# app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')
@app.route("/")
def home():
    return render_template('home.html' ,current_page='home')


@app.route('/products')
def products():
   return render_template('products.html',current_page='products')

@app.route('/partnerships')
def partnerships():
   return render_template('partnerships.html',current_page='partnerships')

@app.route('/accessibility')
def accessibility():
   return render_template('accessibility.html',current_page='accessibility')


@app.route('/about-us')
def aboutUs():
   return render_template('about-us.html',current_page='aboutUs')

@app.route('/contact-us')
def contactUs():
   return render_template('contact-us.html',current_page='contactUs')


if __name__ == '__main__':
  app.run(debug=True)