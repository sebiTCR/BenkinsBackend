from jinjax import Catalog

from core import log


class Renderer:
    _catalog: Catalog = None

    def __new__(cls, env=None):
        if cls._catalog is None:
            cls._catalog = Catalog(jinja_env=env)
            cls._catalog.add_folder("./web/components")
            log.debug("Catalog loaded", file=__name__)
        return cls._catalog

    def render_component(self, *args):
        return self._catalog.render(*args)


    def render_assets(self):
        return self._catalog.render_assets()


renderer = Renderer()
catalog = None
