# Install

Create a virtual env:
`python -m venv env`

Activate it:
`source env/bin/activate`

Install required dependencies:
`recorder/install.sh`

The script assumes that the device is mapped on `/dev/ttyUSB0`.
Run it with `python recorder/gqgmc-recorder.py`, it will output one CPM mesures each seconds for 2 minutes.

Deactivate the virtual env:
`deactivate`
