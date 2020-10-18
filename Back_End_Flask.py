from flask import Flask, render_template,request, jsonify
from DB_Hand_Mongo import Ext_DB_token

	#------------------------APP CONFIG----------------------------#
DEBUG = True
app = Flask(__name__,
			static_folder='static/',
            template_folder='templates/')
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '123'

@app.route('/', methods=['POST','GET'])
def form_post():
	if request.method == 'POST':
		UserToken = request.form
		tok = UserToken['UserToken']
		print(tok)
		Acc = Ext_DB_token(tok)
		if Acc != None:
			Tipo_Acc = Acc[2].upper()
			return jsonify({'Tipo_Acc':Tipo_Acc,
					'User':Acc[0],
					'Pass':Acc[1]}),200
		else:
			return jsonify({'error':'Not found account'}),404
	elif request.method == 'GET':
		return render_template('hello2.html')

@app.errorhandler(404)
def page_not_found(error):
	return 'Página no encontrada...'

if __name__ == '__main__':
	app.run(debug=True,threaded=True)
	#app.run(host='0.0.0.0',port=5000,debug=True)
