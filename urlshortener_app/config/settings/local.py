import sys

from .common import *

TESTING = len(sys.argv) > 1 and sys.argv[1] == "test"

if not TESTING and DEBUG:
    MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"] + MIDDLEWARE
    INSTALLED_APPS += ["debug_toolbar"]


def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
}

INTERNAL_IPS = ["localhost", "0.0.0.0"]
