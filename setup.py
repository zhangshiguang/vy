#! /usr/bin/env python

from distutils.core import setup

setup(name="vy",
      version="3.6.0",
      description="A vim-like in python made from scratch.",
      packages=["vyapp", 
                "vyapp.plugins",
                "vyapp.plugins.syntax",
                "vyapp.plugins.spawn",
                "vyapp.plugins.syntax.styles",
                "vyapp.plugins.pdb"],
      scripts=['vy'],
      package_data={'vyapp': ['vyrc']},
      author="Iury O. G. Figueiredo",
      author_email="ioliveira@id.uff.br",
      url='https://github.com/vyapp/vy',
      download_url='https://github.com/iogf/vy/releases',
      keywords=['vy', 'vi', 'vim', 'emacs', 'sublime', 'atom', 'nano', 'vim-like'],
      classifiers=[])













