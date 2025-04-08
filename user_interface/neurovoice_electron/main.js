const { app, BrowserWindow } = require('electron');
const { spawn } = require('child_process');
const path = require('path');

let djangoProcess;

function createWindow() {
    const mainWindow = new BrowserWindow({
        width: 400,
        height: 800,
        minWidth: 400,
        minHeight: 800,
        resizable: false,
        show: false,
        center: true,
        webPreferences: {
            nodeIntegration: true
        }
    });

    mainWindow.loadURL('http://127.0.0.1:8000/'); // Django local server

    mainWindow.once('ready-to-show', () => {
        mainWindow.show();
    })
}

function startDjangoServer() {
    const djangoPath = path.join(__dirname, '../');
    djangoProcess = spawn('python', ['manage.py', 'runserver'], {cwd: djangoPath});

    djangoProcess.stdout.on('data', (data) => {
        console.error(`Django error: ${data}`);
    });
}

app.whenReady().then(() => {
    startDjangoServer();
    setTimeout(createWindow, 3000);
});

app.on('window-all-closed', () => {
    if (djangoProcess) {
        spawn("taskkill", ["/pid", djangoProcess.pid, '/f', '/t']);
    }

    if (process.platform !== 'darwin') app.quit();
});