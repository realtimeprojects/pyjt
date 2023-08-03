import sys
import os
import shlex

sys.path.append(".")
sys.path.append("..")

source_suffix = '.rst'

master_doc = 'index'

project = u'pyjt'
copyright = u'2023, Claudio Klingler'
author = u'Claudio Klingler'

extensions = [ 'sphinx.ext.autodoc', 'sphinx.ext.autosummary', 'sphinx.ext.napoleon' ]

napoleon_google_docstrings = False
napoleon_use_param = False
napoleon_use_ivar = True

