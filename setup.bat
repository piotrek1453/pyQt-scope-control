@ECHO OFF
pip install pyqt5 pyqt5-tools pyvisa pyvisa-py
python -m virtualenv --system-site-packages venv
venv/Scripts/activate
pip -r requirements.txt
PAUSE