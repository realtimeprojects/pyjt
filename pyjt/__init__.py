# flake8: noqa: F401
import os
import importlib
import jpype
import jpype.imports

def start():
    """ Start the pyjt JVM.

        Needs to be called before using pyjt.
    """
    jpype.startJVM(jpype.getDefaultJVMPath(), f"-Djava.class.path={os.environ.get('CLASSPATH', '')}")


def run(app, args=[""]):
    module = importlib.import_module(app)
    module.main(args)

def shutdown():
    jpype.shutdownJVM()

from .Proxy import Proxy
from .Frame import Frame, FrameFinder
from .Fixture import Fixture
from .ComponentFinder import Locator
from .Inspector import Inspector
