# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from material.model import Material

def vitrine(_write_tmpl, pesquisa):
    materiais = Material.query(Material.nome >= pesquisa).order(Material.nome).fetch()
    dict = {'materiais': materiais}
    _write_tmpl('/home/lista', dict)



def cadastrar_material(_write_tmpl):
    _write_tmpl('/templates/lista.html')

def salvar_material(_handler, nome, descricao, quantidade):
    quantidade = (quantidade)
    material = Material(nome=nome, descricao=descricao, quantidade=quantidade)
    material.put()



