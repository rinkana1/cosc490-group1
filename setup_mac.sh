echo Setting up Python virtual environment...
python -m venv env
source env/Scripts/activate

echo Installing python dependencies...
pip install -r requirements.txt

echo Installing FFMPEG...
brew install ffmpeg

echo Installing Electron dependencies...
cd neurovoice_electron
npm install

echo Setup complete.