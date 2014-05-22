
from __future__ import absolute_import, unicode_literals




 def teste_mock(self):
        obj=Mock()
        obj.atributo.calcular('soma',1,2)
        obj.atributo.calcular.assert_called_once_with('soma',1,2)