import time
import logging

from pyjt.Proxy import Proxy

log = logging.getLogger(__name__)


class Locator:
    def __init__(self, **kwargs):
        self._filters = kwargs
        self._contains = []

    def update(self, **kwargs):
        self._filters.update(**kwargs)

    def contains(self, **kwargs):
        self._contains.append(Locator(**kwargs))
        return self

    def matches(self, component):
        if not self._has(component):
            return False

        for locator in self._contains:
            log.debug(f"contains {locator}")
            if ComponentFinder._locate(window=component, locator=locator) is None:
                return False
        return True

    def _has(self, component):
        return _matches(component, **self._filters)

    def __repr__(self):
        return f"Locator({self._filters})"


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
    DEFAULT_TIMEOUT = 5
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
            return check
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
