from flask import Flask,request
from caesar import rotate_string

app=Flask(__name__)


form="""
<head>
<style>
.layout{{
    margin:0 auto;
    width:30%;
    background-color:#EEEEEE;
    padding:20px;
    border-radius:10px
}}
textarea{{
    margin:10px 0;
    width:400px;
    height:100px;

}}
.error{{
color:red;
}}
</style>
</head>
<body>
<div class='layout'>
<form method="post">
<label for="rot">Rotate by:</label>
<input type="text" name="rot" value="0">
<br>
<p class='error'>{0}</p>
<br>
<textarea type="text" name="text">{1}</textarea>
<br>
<input type="submit">

</form>
</div>
</body>
"""

@app.route('/')
def index():
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
