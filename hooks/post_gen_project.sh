#!/usr/bin/env bash
set -e

WAGTAIL="{{ cookiecutter.wagtail }}"

if [ "$WAGTAIL" == "y" ]; then
    # Wagtail requested - use the wagtail base HTML file with extra tags
    mv templates/base_wagtail.html templates/base.html
    # And remove non-wagtail templates
    rm -f templates/homepage.html
else
    # No wagtail - remove any wagtail related files
    rm -f apps/core/monkeypatch.py
    rm -rf apps/pages
    rm -rf apps/settings
    rm -rf templates/blocks
    rm -rf templates/pages
    rm -rf templates/wagtail
    rm -f templates/base_wagtail.html
fi
