import idom

from . import BUNDLE_PATH, FALLBACK, MODULE_NAME, PRODUCTION, VERSION

_web_module = None


def _load_web_module():
    global _web_module
    # reload in development
    if PRODUCTION is False:
        from . import get_epoch

        _web_module = idom.web.module_from_file(
            name=f"{MODULE_NAME}.{get_epoch()}", file=BUNDLE_PATH, fallback=FALLBACK
        )
    # load once in production
    elif _web_module is None:
        _web_module = idom.web.module_from_url(
            url=f"https://meganno-ui.s3.amazonaws.com/meganno_ui@{VERSION}.js",
            fallback=FALLBACK,
        )
    return _web_module


def load_component(name: str = ""):
    web_module = _load_web_module()
    return idom.web.export(web_module, name)
