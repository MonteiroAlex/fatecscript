# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from material.model import Material
import json

def get_all_material(_write_tmpl):

    materiais = Material.query().fetch()
    _write_tmpl(json.dumps(materiais))





def salvar_material( nome, descricao, quantidade):
    material = Material(nome=nome, descricao=descricao, quantidade=quantidade)
    material.put()



