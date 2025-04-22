echo Setting up Python virtual environment...
python3 -m venv env
source env/Scripts/activate

echo Installing python dependencies...
pip install -r requirements.txt

echo Installing FFMPEG...
sudo apt update
sudo apt install ffmpeg

echo Installing Electron dependencies...
cd neurovoice_electron
npm install

echo Setup complete.