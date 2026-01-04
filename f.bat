@echo off
echo Scaffolding for RTT linux super shell
md packages
cd packages
md wrsadc-shell
cd wrsadc-shell
copy con wrsadc_shell.sh
copy con install.sh
copy con README.md
copy con package.json
cd..
md wrsadc-python
cd wrsadc-python
copy con wrsadc_core.py
copy con __init__.py
copy con setup.py
copy con README.md
cd..
md tft-3pack
cd tft-3pack
copy con TFT_Primitive_1.md
copy con TFT_Primitive_2.md
copy con TFT_Primitive_3.md
cd..
md wrsadc_integration
cd wrsadc_integration
copy con wrsadc_core.py
copy con wrsadc_shell.sh
cd..
copy con README.md
cd docs
md RTT
md Triadic
md Hesadic
