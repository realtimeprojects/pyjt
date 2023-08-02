import jpype
import logging

log = logging.getLogger(__name__)


class Proxy:
    """ Proxy calls to the java.awt and javax.swing libraries using
        the event thread to ensure thread-safety.

        This class is usually automatically instanciated and returned
        by the locate() and find() functions of pyjt.

        If the proxy detects that the return value of the call
        is a instance of java.awt.Component, a new proxy instance
        for this object is created and returned.

        Example:

            proxy = Proxy(java.swing.JLabel())
            text = proxy.getText()
    """
    def __init__(self, instance):
        """ Create a new proxy.

            :param instance: The instance of a java.awt.* or java.swing.* class
                             to proxy call to.
         """
        self._instance = instance

    @property
    def instance(self):
        return self._instance

    def __getattr__(self, name):
        import javax
        import java

        @jpype.JImplements(java.lang.Runnable)
        class _Launch:
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

        fnc = getattr(self._instance, name)

        def _savecall(*args, **kwargs):
            # log.debug(f"proxying call: {name}({args}, {kwargs})")
            launcher = _Launch(fnc, *args, **kwargs)
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
    import java
    if isinstance(element, java.awt.Component):
        return Proxy(element)
    return element
