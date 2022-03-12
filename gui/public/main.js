const {app, BrowserWindow, ipcMain} = require('electron');
const path = require('path');
const url = require('url');

const fs = require('fs');

require('@electron/remote/main').initialize()

function createWindow() {
  console.log('Application has started');

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


// temporary variable to store data while background
// process is ready to start processing
let cache = {
	data: undefined
};

// This event listener will listen for request
// from visible renderer process App.js
ipcMain.on('START_BACKGROUND_VIA_MAIN', (event, args) => {
	const backgroundFileUrl = url.format({
		pathname: path.join(__dirname, `../background_tasks/run_script.html`),
		protocol: 'file:',
		slashes: true,
	});
	hiddenWindow = new BrowserWindow({
		show: true,
		webPreferences: {
      nodeIntegration: true,
      enableRemoteModule: true,
      contextIsolation: false,
		},
	});
	hiddenWindow.loadURL(backgroundFileUrl);

	hiddenWindow.webContents.openDevTools();

	hiddenWindow.on('closed', () => {
		hiddenWindow = null;
	});

	cache.data = args;
});


// This event listener will listen for data being sent back
// from the background renderer process
ipcMain.on('MESSAGE_FROM_BACKGROUND', (event, args) => {
	// mainWindow.webContents.send('MESSAGE_FROM_BACKGROUND_VIA_MAIN', args);
  console.log("Python Return:")
  console.log(args);
});


// Listening for background ready
ipcMain.on('BACKGROUND_READY', (event, args) => {
	event.reply('START_SCRIPT', {
		data: cache.data,
	});
});

// Call from Render (App.js) to read files at dir path
ipcMain.on('READ_FILES', (event, args) => {
  const path = '/Users/rileybusche/Development/nmr_data_analysis/LVR_Diffusion/';
  var phFolders = [];
  const re = new RegExp('ph[0-9]');
  // const re = /ph/ + /^-?[0-9]+.?[0-9]*$/g
  fs.readdir(path, (err, files) => {
    files.forEach(file => {
      // Send Files Back to Renderer Thread in MainContainer.js
      if (file.match(re) !== null) {
        phFolders.push(file);
        console.log(file)
      }
      // console.log(file);
    });
    // Pune any files/folders that are not ph*
    event.reply('PH_VALUES_RETURN', phFolders);
  });
});