import jpype
import logging

import java
import javax

log = logging.getLogger(__name__)


@jpype.JImplements(java.lang.Runnable)
class Launch:
    def __init__(self, func, *args, **kwargs):
        self._func = func
        self._args = args
        self._kwargs = kwargs
        self._ret = None

    @jpype.JOverride
    def run(self):
        try:
            self._ret = self._func(*self._args, **self._kwargs)
        except Exception as ee:
            log.error(str(ee))
            raise ee


class Proxy:
    def __init__(self, instance):
        self._instance = instance

    @property
    def instance(self):
        return self._instance

    def __getattr__(self, name):
        fnc = getattr(self._instance, name)

        def _savecall(*args, **kwargs):
            # log.debug(f"proxying call: {name}({args}, {kwargs})")
            launcher = Launch(fnc, *args, **kwargs)
            javax.swing.SwingUtilities.invokeAndWait(launcher)
            ret = launcher._ret
            # log.debug(f"\tret is {ret} {type(ret)}")
            if hasattr(ret, "__iter__"):
                # log.info("\tlist detected!")
                return [_proxitise(element) for element in ret]
            return _proxitise(ret)
        return _savecall

    def __repr__(self):
        return f"{type(self._instance)}: {self.getName()}"


def _proxitise(element):
    if isinstance(element, java.awt.Component):
        return Proxy(element)
    return element
