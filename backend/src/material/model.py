from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
import json

class Material(ndb.Model):
    nome = ndb.StringProperty()
    descricao = ndb.StringProperty()
    quantidade = ndb.StringProperty()



    @classmethod
    def query_ordenada_por_nome(cls):
        return cls.query().order(cls.nome)


class Usuario(ndb.Model):

    nome = ndb.StringProperty()
    email = ndb.StringProperty()
    google_id = ndb.StringProperty()



