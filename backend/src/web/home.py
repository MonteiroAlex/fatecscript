# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from web import my_form
from tekton import router


def index(_write_tmpl):
    url = router.to_path(my_form)
    _write_tmpl('templates/home.html', {'form_url': url})


def params(_resp, *args, **kwargs):
    _resp.write(args)
    _resp.write(kwargs)


def hist(_write_tmpl):
    _write_tmpl('/templates/historia.html')

def contato(_write_tmpl):
    _write_tmpl('/templates/contato.html')


def infra(_write_tmpl):
    _write_tmpl('/templates/infra.html')

def ensino(_write_tmpl):
    _write_tmpl('/templates/ensino.html')

def extra(_write_tmpl):
    _write_tmpl('/templates/extra.html')

def lista(_write_tmpl):
    _write_tmpl('/templates/lista.html')

def agenda(_write_tmpl):
    _write_tmpl('/templates/agenda.html')

def galeria(_write_tmpl):
    _write_tmpl('/templates/galeria.html')

def menu(_write_tmpl):
    _write_tmpl('/templates/home.html')