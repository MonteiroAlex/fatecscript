from __future__ import absolute_import, unicode_literals
from web import my_form
from tekton import router
from livro.model import  Livro
import json


def index(_write_tmpl):

	livros = Livro.query()
	for l in livros:
		l.id = l.key.id()

	var = {"saveLink":"/livrocad/post_salvar",
	       "livros":livros}
	_write_tmpl('templates/admin/livrocad.html', var)

def post_salvar(_handler, autor, titulo, editora, paginas):

	livro = Livro(autor=autor, titulo=titulo, editora=editora, paginas=int(paginas))
	livro.put()

	_handler.redirect("/livrocad")

def salvar(_resp, autor, titulo, editora, paginas):

	livro = Livro(autor=autor, titulo=titulo, editora=editora, paginas=int(paginas))
	key = livro.put() # .put() retorna a key do objeto

	json_str = json.dumps({'id':key.id()})

	_resp.write(json_str)

def listar(_resp):

	json_struct = []

	livros = Livro.query()
	for l in livros:
		json_struct += [{"autor":l.autor,
		        "titulo":l.titulo,
		        "editora":l.editora,
		        "paginas":l.paginas,
		        "idLivro":l.key.id()}]

	json_str = json.dumps(json_struct)
	_resp.write(json_str)

def editar(_resp, idLivro, autor, titulo, editora, paginas):

	livro = Livro.get_by_id(int(idLivro))

	livro.autor = autor
	livro.titulo = titulo
	livro.editora = editora
	livro.paginas = int(paginas)

	livro.put()

	# Não acho que precise de retorno

def remover(_resp, idLivro):

	livro = Livro.get_by_id(int(idLivro))

	livro.key.delete()
