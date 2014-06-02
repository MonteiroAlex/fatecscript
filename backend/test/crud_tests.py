
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from curso.model import Curso
from mock.mock import Mock

import tmpl
from usuario.model import Usuario
from web.curso import rest, crud, rest


class SalvarTests(GAETestCase):
    def test_sucesso(self):
        usuario_logado = Usuario()
        usuario_logado.put()
        handler = Mock()
        crud.salvar(handler, usuario_logado, 'INFORMATICA', 'BASICA')
        cursos = Curso.query().fetch()
        self.assertEqual(1, len(cursos))
        curso = cursos[0]
        self.assertEqual('INFORMATICA', curso.nome)
        self.assertEqual('BASICA', curso.descricao)
        handler.redirect.assert_called_once_with('/curso')


class listarTests(GAETestCase):
    def test_sucesso(self):
        usuario_logado = Usuario()
        usuario_logado.put()
        handler = Mock()
        crud.salvar(handler, usuario_logado, 'INFORMATICA', 'BASICA')
        cursos = Curso.query().fetch()
        self.assertEqual(1, len(cursos))
        curso = cursos[0]
        self.assertEqual('INFORMATICA', curso.nome)
        self.assertEqual('BASICA', curso.descricao)
        rest.listar_cursos(handler,usuario_logado)
        handler.redirect.assert_called_once_with('/curso')


