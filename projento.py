from flask import Flask, jsonify 

app= Flask(__name__)

livro=[
    {
    'id' :1,
    'titulo': 'livro de receita',
    'autor' :'erick jackar'
    }
]

# consultar (todos)
@app.route('/livro',methods=['GET'])
def obter_livros():
    return jsonify(livro)


app.run(port=5000,host='localhost',debug=True)