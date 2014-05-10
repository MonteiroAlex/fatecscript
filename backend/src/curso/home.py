__author__ = 'Alex'
from __future__ import absolute_import, unicode_literals
from curso.model import Curso
from tekton import router
from curso.crud import salvar, detalhar


def index(_write_tmpl, _usuario_corrente):
    salvar_path = router.to_path(salvar)
    query = Curso.query_encontrar_cursos_de_usuario(_usuario_corrente.key)
    cursos = query.fetch()
    for c in cursos:
        c.detalhar_path = router.to_path(detalhar, c.key.id())
    _write_tmpl('/home/detalhe', {'cursos': cursos, 'salvar_path': salvar_path})