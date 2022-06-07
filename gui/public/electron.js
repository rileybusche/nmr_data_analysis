const {app, BrowserWindow, ipcMain} = require('electron');
const isDev = require('electron-is-dev');
const path = require('path');
const fs = require('fs');
const url = require('url');
require('@electron/remote/main').initialize();

// This is to differentiate if it is in DEV or Prod if there is a need to loop through all
// const possibilities = [
//     path.join(process.resourcePath, "python", "bin", "python3.9"),
//     // In development
//     // path.join(__dirname, "python", "bin", "python3.9"),
// ]
// for (const path of possibilities) {
//     if (fs.existsSync(path)) {
//       return path;
//     }
// }
bundledPython = path.join(process.resourcesPath, "python", "bin", "python3.9");

bundledPath = fs.existsSync(bundledPython) ? bundledPython : "python3";

// temporary variable to store data while background
// process is ready to start processing
let cache = {
	jsonPath: undefined,
  samplePath: undefined,
  scriptPath: path.join(__dirname, '..', '..', 'app.asar.unpacked', 'build', 'scripts', 'main.py'),
  bundledPythonPath: bundledPath
  // scriptPath: path.join(__dirname, '..', '..', 'main'),
};

function createWindow() {
  // Create the browser window.
  console.log('Window has started');
  globalThis.win = new BrowserWindow({
    width: 1100,
    height: 800,
    title: 'NMR Analysis',
    webPreferences: {
      nodeIntegration: true,
      enableRemoteModule: true,
      contextIsolation: false,
    },
  });
  // Serve window
  const URL = isDev
  ? 'http://localhost:3000/'
  : `file://${path.join(__dirname, '../build/index.html')}`;
  win.loadURL(URL);
  // win.loadURL('http://localhost:3000/');
}

// Store Data in json file for python script to read from
function writeDataToFile(data) {
  const jsonPath = path.join(__dirname, '..', '..', 'app.asar.unpacked', 'build', 'data.json');
  console.log('Writing JSON Data to: ', jsonPath);
  console.log(data)

  fs.writeFileSync(jsonPath, JSON.stringify(data, null, 4));
  cache.jsonPath = jsonPath;
  console.log('JSON Data path sent to python script: ', cache.jsonPath);

  var data = JSON.parse(fs.readFileSync(jsonPath));
  console.log(JSON.stringify(data, null, 4));
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

ipcMain.setMaxListeners(0)

// Builds a Render Window to handle Python Script Processing
ipcMain.on('START_BACKGROUND_VIA_MAIN', (event, args) => {
  globalThis.modalWindow = new BrowserWindow({
    show: true,
    autoHideMenuBar: true,
    frame: false,
    parent: win,
    modal: true,
    width: 500,
    height: 300,
    transparent: true,
    title: 'Analyzing...',
    webPreferences: {
      nodeIntegration: true,
      enableRemoteModule: true,
      contextIsolation: false,
    },
  });
  // For windows, the '#' needs to be formated with `hash:`
  const osURL = process.platform === "win32"
    ? url.format({
      pathname: path.join(__dirname, '..', 'build', 'index.html'),
      protocol: 'file:',
      slashes: true,
      hash: '/python'
    })
    : `file://${path.join(__dirname, '../build/index.html#/python')}`;

  const URL = isDev
    ? 'http://localhost:3000/python'
    : osURL;

  // Show Modal Window
  modalWindow.loadURL(URL);
  modalWindow.on('closed', () => {
		modalWindow = null;
  });

});

// Listening for modal ready
// Reply and start script
ipcMain.on('MODAL_READY', (event, args) => {
	event.reply('START_SCRIPT', {
		data: cache
	});
});

ipcMain.on('CLOSE_MODAL', (event, args) => {
  BrowserWindow.getFocusedWindow().close();
});
// This event listener will listen for request
// from visible renderer process App.js
ipcMain.on('SAVE_DATA', (event, args) => {
  writeDataToFile(args);
});

// This event listener will listen for data being sent back
// from the background renderer process
ipcMain.on('MESSAGE_FROM_BACKGROUND', (event, args) => {
	// mainWindow.webContents.send('MESSAGE_FROM_BACKGROUND_VIA_MAIN', args);
  console.log("Python Return:")
  console.log(args);
});

// Call from Render (App.js) to read files at dir path
ipcMain.on('READ_FILES', (event, args) => {
  // const path = '/Users/rileybusche/Development/nmr_data_analysis/LVR_Diffusion/';
  const filePath = path.dirname(args);
  cache.samplePath = filePath;
  // console.log('Path: ', args);
  // console.log('Path DirName: ', path.dirname(args));
  var phFolders = [];

  // Matching PH folders
  const re = /ph[0-9]/gi;
  fs.readdir(filePath, (err, files) => {
    files.forEach(file => {
      // Pune any files/folders that are not ph*
      if (file.match(re) !== null) {
        phFolders.push(file);
      }
    });
    // Sort Files in order
    console.log(phFolders);
    phFolders.sort(function (a, b) {
      const re = /^-?[0-9]+.?[0-9]*$/g;
      if (parseFloat(a.split('h')[1]) > parseFloat(b.split('h')[1]))
        return 1;
      if (parseFloat(b.split('h')[1]) > parseFloat(a.split('h')[1]))
        return -1;
      return 0;
    });
    console.log(phFolders);
    // Send Files Back to Renderer Thread in MainContainer.js
    event.reply('PH_VALUES_RETURN', phFolders); 
  });
});