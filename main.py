from flask import *
import json
import os

global __dirname
__dirname = os.path.dirname(os.path.realpath(__file__))   #directory

app = Flask(__name__)

@app.route("/")
def main():
    return render_template_string("""\
    <style>
        body {
            text-align: center;
        }
    </style>
    <body>
        <h1>IP Data API</h1>
        <h2>Read the readme.md for more informantion</h2>
        <a href=/manual_search>Manual Search</a>
    </body>
    """)
    
@app.route("/manual_search")#manual seach explained in the readme
def search():
    return render_template_string("""\
    <form action="/data" method="get">
        <input type=text name="lookup">
        <input type=submit value="submit">
    </form>
    """)

@app.route("/data", methods=["GET"])
def data():
    try:
        to_search = request.args.get('lookup')#searching for the data
        with open(__dirname + '\\data.json') as f:
            json_string = json.load(f)
           
            for x in json_string["data"]:
                json_string_data = json_string
                
                if to_search in x.keys():    
                    string = x
                    break
                else:
                    string = "not in our data"
                    
        return render_template_string("""\
        {{%s}}
        """ % (string))#print the data
        
    except:
        return render_template_string("""\
        Check if the get request is in the url.
        """)
app.run(debug=False)