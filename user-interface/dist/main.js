"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var Main = /** @class */ (function () {
    function Main() {
    }
    Main.onWindowAllClosed = function () {
        if (process.platform !== 'darwin') {
            Main.application.quit();
        }
    };
    Main.onClose = function () {
        Main.mainWindow = null;
    };
    Main.onReady = function () {
        Main.mainWindow = new Main.BrowserWindow({ width: 800, height: 600 });
        Main.mainWindow
            .loadURL('file://' + __dirname + '/../src/html/index.html');
        Main.mainWindow.on('closed', Main.onClose);
    };
    Main.main = function (app, browserWindow) {
        Main.BrowserWindow = browserWindow;
        Main.application = app;
        Main.application.on('window-all-closed', Main.onWindowAllClosed);
        Main.application.on('ready', Main.onReady);
    };
    return Main;
}());
exports.default = Main;
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
//# sourceMappingURL=main.js.map