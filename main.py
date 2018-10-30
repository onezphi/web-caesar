from flask import Flask, request
from caesar import rotate_string


app=Flask(__name__)

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}

        </style>
    </head>
    <body>
    <div class='layout'>
    <form method="post">
    <label for="rot">Rotate by:</label>
    <input type= "text" name = "rot" value = "0">
    <p class='error'>{0}</p>       
           
    <textarea type = "text" name = "text">{1}</textarea>
       
        <input type = "submit">
        </form>
        </div>
   
    </body>
</html>

"""

@app.route("/")
def index():
    encrypted_text=''
    return form.format('','')

@app.route('/',methods=['POST'])
def encrypt():
    rot=request.form['rot']
    text=request.form['text']
    if ' ' in rot or not rot.isdigit():
        return form.format('Error in rotation value','')
    encrypted_text=rotate_string(text,int(rot))
    return form.format('',encrypted_text)
if __name__=='__main__':

    app.run(debug=True)    



