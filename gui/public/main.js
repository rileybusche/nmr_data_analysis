const {app, BrowserWindow, ipcMain} = require('electron');
const path = require('path');
const url = require('url');

const fs = require('fs');

require('@electron/remote/main').initialize();

// temporary variable to store data while background
// process is ready to start processing
let cache = {
	jsonPath: undefined
};

function createWindow() {
  console.log('Application has started');

  // Create the browser window.
  const win = new BrowserWindow({
    width: 1100,
    height: 800,
    webPreferences: {
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

// Store Data in json file for python script to read from
function writeDataToFile(data) {
  const path = __dirname + '/data.json';
  console.log('Writing Data to: ', path);
  console.log(data)

  fs.writeFileSync(path, JSON.stringify(data, null, 4));
  cache.jsonPath = path;
  console.log('Path sent to python script: ', cache.jsonPath);
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

  writeDataToFile(args);
});


// This event listener will listen for data being sent back
// from the background renderer process
ipcMain.on('MESSAGE_FROM_BACKGROUND', (event, args) => {
	// mainWindow.webContents.send('MESSAGE_FROM_BACKGROUND_VIA_MAIN', args);
  console.log("Python Return:")
  console.log(args);
});


// Listening for background ready
// Calls to run_script.html
ipcMain.on('BACKGROUND_READY', (event, args) => {
	event.reply('START_SCRIPT', {
		data: cache.jsonPath
	});
});

// Call from Render (App.js) to read files at dir path
ipcMain.on('READ_FILES', (event, args) => {
  // const path = '/Users/rileybusche/Development/nmr_data_analysis/LVR_Diffusion/';
  const filePath = path.dirname(args);
  // console.log('Path: ', args);
  // console.log('Path DirName: ', path.dirname(args));
  var phFolders = [];
  // Matching PH folders
  const re = new RegExp('ph[0-9]');
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
    // 'MaxListenersExceededWarning: Possible EventEmitter memory leak detected. 
    // 11 PH_VALUES_RETURN listeners added to [EventEmitter]. Use emitter.setMaxListeners() to increase limit' 
    // ... May end up being a problem.
  });
});