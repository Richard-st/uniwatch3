from app import app, render_template


@app.route('/', methods=['GET', 'POST'])
def index():
    #return "hello from views.py"
    return render_template('index.html',text='From Index')
