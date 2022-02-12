const {app, BrowserWindow, ipcMain} = require('electron')
const path = require('path')

const {PythonShell} = require('python-shell');

let pyshell = new PythonShell('python.py');

require('@electron/remote/main').initialize()

function createWindow() {
  console.log('Application has started');

  // var python = require('child_process').spawn('python', ['./python.py']);
  // python.stdout.on('data',function(data){
  //   console.log("data: ",data.toString('utf8'));
  //   console.log('Test');
  // });
  // Create the browser window.
  const win = new BrowserWindow({
    width: 1100,
    height: 800,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      nodeIntegration: true,
      enableRemoteModule: true,
      contextIsolation: false,
    },
  });

  // and load the index.html of the app.
  // win.loadFile("index.html");
  // win.loadURL(
  //   isDev
  //     ? 'http://localhost:3000'
  //     : `file://${path.join(__dirname, '../build/index.html')}`
  // );
  // // Open the DevTools.
  // if (isDev) {
  //   win.webContents.openDevTools({ mode: 'detach' });
  // }
  win.loadURL('http://localhost:3000')
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.whenReady().then(createWindow);

// Quit when all windows are closed, except on macOS. There, it's common
// for applications and their menu bar to stay active until the user quits
// explicitly with Cmd + Q.
app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    console.log('Application has started');
    createWindow();
  }
});

ipcMain.on('OSC_VOLTAGE_DATA', (event, args) => {
  mainWindow.webContents.send('OSC_VOLTAGE_DATA', args);
});