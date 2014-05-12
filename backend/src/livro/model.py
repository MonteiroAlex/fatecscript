from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb

class Livro(ndb.Model):

	autor = ndb.StringProperty();
	titulo = ndb.StringProperty();
	editora = ndb.StringProperty();
	paginas = ndb.IntegerProperty();
