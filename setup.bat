@ECHO OFF
pip install pyqt5 pyqt5-tools pyvisa pyvisa-py pyvisa_sim virtualenv
python -m virtualenv venv --system-site-packages
venv/Scripts/activate
pip install -I -r requirements.txt
PAUSE