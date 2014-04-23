# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import tmpl_middleware

from usuario import middleware
from tekton.gae.middleware import router_middleware, parameter, webapp2_dependencies, email_errors


SENDER_EMAIL = 'alexsandromonteiro.m@gmail.com'
WEB_BASE_PACKAGE = "web"
MIDDLEWARES = [middleware.execute,
               tmpl_middleware.execute,
               email_errors.execute,
               webapp2_dependencies.execute,
               parameter.execute,
               router_middleware.execute]

