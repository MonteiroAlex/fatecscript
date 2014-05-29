from __future__ import absolute_import, unicode_literals
from curso.model import Curso
from tekton import router
from web.curso.crud import salvar, detalhar


def index(_write_tmpl, _usuario_logado):
    salvar_path = router.to_path(salvar)
    query = Curso.query_encontrar_cursos_de_usuario(_usuario_logado.key)
    cursos = query.fetch()
    for c in cursos:
        c.detalhar_path = router.to_path(detalhar, c.key.id())
    _write_tmpl('/home/curso', {'cursos': cursos, 'salvar_path': salvar_path})