@echo off
echo Commands:
echo.
echo python -m pip install pytest
echo python -m pytest -q
echo.
echo.
echo These tests protect the important invariant: we rewrite .md targets only inside const DOC_MAP, not every .md occurrence in an index.html file.
echo python -m py_compile scripts\build_html_mirror*py
echo No output means it compiled successfully. Then:
echo python -m pytest -q
echo.
echo And finally our mirror invariant:
echo python scripts\build_html_mirror.py --check*
