import time
import logging

from pyjt.Proxy import Proxy

log = logging.getLogger(__name__)


class Locator:
    def __init__(self, **kwargs):
        self._filters = kwargs
        self._contains = []
        self._has = []

    def update(self, **kwargs):
        self._filters.update(**kwargs)

    def contains(self, **kwargs):
        """ Ensure the control has a sub-component with the given attributes
            somewhere in the tree.
        """
        self._contains.append(Locator(**kwargs))
        return self

    def has(self, **kwargs):
        """ Ensure the control has a directo sub-component with the given
            attributes.
        """
        self._has.append(Locator(**kwargs))
        return self

    def matches(self, component):
        if not _matches(component, **self._filters):
            return False

        log.debug(f"found {component}, checking childs...")
        for locator in self._contains:
            log.debug(f"contains {locator}")
            if ComponentFinder._locate(window=component, locator=locator) is None:
                return False

        for locator in self._has:
            log.debug(f"has {locator}")
            if not _child_matches(component, locator):
                return False
        return True

    def __repr__(self):
        return f"Locator({self._filters})"


def _child_matches(component, locator):
    log.debug(f"_child_matches({component}, {locator}")
    for subcontrol in component.getComponents():
        if locator.matches(subcontrol):
            log.debug(f"_child_matches({component}, {locator}: found {subcontrol}")
            return True
    log.debug(f"_child_matches({component}, {locator}: FAILED")
    return False


class Timer:
    def __init__(self, timeout=None, cycle=None):
        self._timeout = timeout
        self._cycle = cycle
        self._first = True

    def start(self):
        self._started = time.time()
        return self

    def elapsed(self, seconds=None):
        if not self._first:
            time.sleep(self._cycle)
        self._first = False
        now = time.time()
        timeout = seconds if seconds else self._timeout
        return self._started + timeout <= now


class ComponentFinder:
    DEFAULT_TIMEOUT = 1
    DEFAULT_DELAY = 1

    @staticmethod
    def find(window, locator=None, timeout=None, **kwargs):
        timeout = timeout if timeout else ComponentFinder.DEFAULT_TIMEOUT
        timer = Timer(timeout, ComponentFinder.DEFAULT_DELAY).start()
        locator = locator if locator else Locator(**kwargs)

        while not timer.elapsed():
            log.debug(f"retry({locator})")
            hit = ComponentFinder._locate(window, locator)
            if hit is not None:
                return hit
        return None

    @staticmethod
    def findIn(func, locator=None, timeout=None):
        timeout = timeout if timeout else ComponentFinder.DEFAULT_TIMEOUT
        timer = Timer(timeout, ComponentFinder.DEFAULT_DELAY).start()

        while not timer.elapsed():
            log.debug(f"retry({locator})")
            windows = func()
            for window in windows:
                hit = ComponentFinder._locate(window, locator)
                if hit is not None:
                    return hit
        return None

    @staticmethod
    def _locate(window, locator):
        log.debug(f"locate({locator})")
        if locator.matches(window):
            return window
        components = window.getComponents()
        for cmpt in components:
            log.debug(f"found component: {cmpt.getName()} {type(cmpt)}")
            hit = ComponentFinder._locate(cmpt, locator)
            if hit:
                return hit
        return None


@staticmethod
def _matches(cmpt, **kwargs):
    # log.debug(f"_matches({cmpt}, name={name}, text={text})")
    for name, value in kwargs.items():
        if name == 'role':
            cc = cmpt.instance if isinstance(cmpt, Proxy) else cmpt
            log.debug(f"\tcheck01 {name} {type(cc)}={value}")
            check = isinstance(cc, value)
            log.debug(f"\t\tcheck01: {check}")
            if not check:
                return False
            continue
        fname = f"get{name[0].capitalize()}{name[1:]}"
        log.debug(f"check({name}, {value}) -> {fname}: {cmpt}")
        if not hasattr(cmpt, fname):
            log.debug(f"\tcheck({name}) component has no attr {fname}")
            return False
        fnc = getattr(cmpt, fname)
        _value = fnc()
        log.debug(f"\tcheck {value} == {_value}")
        if value is None and _value is None:
            continue
        if not _value:
            return False
        if value not in _value:
            return False
    if not cmpt.isShowing():
        log.debug("\tcheck9")
        return False
    log.debug("\tcheck10")
    return True
