import { BrowserWindow } from 'electron';

export default class Main {
    static mainWindow: Electron.BrowserWindow;
    static application: Electron.App;
    static BrowserWindow;
    private static onWindowAllClosed() {
        if (process.platform !== 'darwin') {
            Main.application.quit();
        }
    }

    private static onClose() {
        Main.mainWindow = null;
    }

    private static onReady() {
        Main.mainWindow = new Main.BrowserWindow({ width: 800, height: 600 });
        Main.mainWindow
            .loadURL('file://' + __dirname + '/../src/html/index.html');
        Main.mainWindow.on('closed', Main.onClose);
    }

    static main(app: Electron.App, browserWindow: typeof BrowserWindow) {
        Main.BrowserWindow = browserWindow;
        Main.application = app;
        Main.application.on('window-all-closed', Main.onWindowAllClosed);
        Main.application.on('ready', Main.onReady);
    }
}

// const

// let mainWindow: BrowserWindow | null;

// function createWindow() {
//     mainWindow = new BrowserWindow({
//         width: 800,
//         height: 600,
//         webPreferences: {
//             nodeIntegration: true
//         }
//     });

//     mainWindow.loadFile(path.join(__dirname, "index.html"));

//     mainWindow.on("closed", () => {
//         mainWindow = null;
//     });
// }

// app.whenReady().then(createWindow);

// app.on("window-all-closed", () => {
//     if (process.platform !== "darwin") {
//         app.quit();
//     }
// });