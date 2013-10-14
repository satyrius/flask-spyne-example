#!/usr/bin/env python
import sys
from app import create_app

app = create_app()

# Hack to run in debug mode on my laptop
# NOTE: THIS NOT FOR PRODUCTION USE
if sys.platform.startswith('darwin'):
    app.debug = True

if __name__ == '__main__':
    app.run()
