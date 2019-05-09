from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:buildit@localhost:3306/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(500))
    

    def __init__(self, title, body):
        self.title = title
        self.body = body
        
        



@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        blog_title = request.form['blogname']
        blog_body = request.form['body']
        blog_post=Blog(blog_title, blog_body)
        
        db.session.add(blog_post)
        db.session.commit()
    
    
    bloglist = Blog.query.all()
    
    
    return render_template('todos.html',title="Bloggy Fresh!", bloglist=bloglist )


@app.route('/bloglists', methods=['GET'])
def bloglisting():
    bloglist = Blog.query.all()
    return render_template('bloglists.html', bloglist=bloglist)

@app.route('/posts', methods=['GET'])
def bloglink():
    blog_id= request.args.get('id')
    print(blog_id)
    blog= get_blog(blog_id)
    return render_template('posts.html', blog = blog)
    

def get_blog(id):
    print(id)
    return Blog.query.get(id)
    



   
if __name__ == '__main__':
    app.run()