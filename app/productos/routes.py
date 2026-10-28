from flask import Blueprint, render_template

productos_bp = Blueprint('productos',__name__,url_prefix="/productos",template_folder="templates")

@productos_bp.route('/')
def lista_productos():
    return render_template('index.html')

@productos_bp.route('/categoria/<categoria>')
def mostrar_categoria(categoria):
    return render_template('categoria.html', categoria=categoria)

