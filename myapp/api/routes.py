from flask import Blueprint

#este es un modulo
api=Blueprint('api',__name__,url_prefix='/api')


#hacemos referencia a qui del modulo para llamar la ruta 
@api.route("/getdata")
def getdata():
    return{'key':'value'}

