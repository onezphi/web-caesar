from flask import Flask, request
from caesar import rotate_string


app=Flask(__name__)
app.config['DEBUG'] = True

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
      #<!-- create your form here -->
      #form uses the post method
      <form methods="post">
      <label for="rot">Rotate by:</label>
      #label on the input element
            <input type= "text" name = "rot" value = "0">
            
            #input element above has a default value of 0
            #per assignment instructions
        
        <textarea type = "text" name = "text">{0}</textarea>
        #second input per the instrux for the body of HTML string
        <input type = "submit">
        </form>
        </div>
    


    </body>
</html>


"""
#wrapped and unwrapped h1 tags to test
#processing the form
@app.route("/")
def index():
    encrypted_text= ''
    return form.format(",")

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


