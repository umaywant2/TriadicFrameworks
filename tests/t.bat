@echo off
echo Commands:
echo.
echo python -m pip install pytest
echo python -m pytest -q
echo.
echo.
echo These tests protect the important invariant: we rewrite .md targets only inside const DOC_MAP, not every .md occurrence in an index.html file.
