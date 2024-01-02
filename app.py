from flask import Flask, render_template,request
from dataset import popular_movies
from  reccomend import reccomend

app = Flask(__name__)
#get the dataset
df=popular_movies()

#now create a route
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/top-movies',methods=['GET','POST'])
def top100_movies():
    #convert the dataframe into html code
    table_html = df.to_html(classes='table table-striped', index=False)

    #then give that table to html
    return render_template('top_movies.html', table=table_html)


@app.route('/reccomend',methods=['GET','POST'])
def reccomend_view():
    if request.method=='POST':
        #retrive the data from the server
        movie_name=request.form['movie_name']

        #give the data to the reccomend function
        Recc=reccomend(movie_name)
        #the data will be in list format eg ['Guardians of the Galaxy', 'Trance', 'The Lego Movie', 'Fantastic Four', 'High-Rise', 'Kung Fu Panda']
         
         #then one by one from the list give the movie names to the reccomend.html so that it could display the movie names
        return render_template('reccomend.html',movie_list=Recc)
    else:
        return render_template('reccomend.html')



if __name__ == '__main__':
    app.run(debug=True)