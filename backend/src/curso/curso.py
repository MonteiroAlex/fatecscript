from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb



def index(_write_tmpl):
    query = Curso.query().order(Curso.nome)
    cursos = query.fetch()

    dct = {'lista_cursos': cursos,
            'matricula_url': router.to_path(matricula),
            'salvar_url': router.to_path(salvar)}
    _write_tmpl('/templates/curso_home.html', dct)



