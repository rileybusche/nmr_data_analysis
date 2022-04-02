import React from "react";

function Python() {
    const { PythonShell } = window.require('python-shell');
    const { ipcRenderer } = window.require('electron');
    const path = require('path');

    console.log("Background Initialized.");
    // This will be called from main.js
    ipcRenderer.on('START_SCRIPT', (event, args) => {
        console.log('Python Shell Created...');
        let pyshell = new PythonShell(path.join(__dirname, '/Users/rileybusche/Development/nmr_data_analysis/gui/scripts/main.py'), {
            pythonPath: 'python3',
            pythonOptions:['-u'], // Gets print results in real time
            args: [args.data]
        });

        pyshell.on('message', function(results) {
            ipcRenderer.send('MESSAGE_FROM_BACKGROUND', { message: results });
        });
        // end the input stream and allow the process to exit
        pyshell.end(function (err,code,signal) {
        if (err) throw err;
        console.log('The exit code was: ' + code);
        console.log('The exit signal was: ' + signal);
        console.log('finished');
        });
    });

    ipcRenderer.send('BACKGROUND_READY');

    return(
        <div>
            <h1>Test for Routing</h1>
        </div>
    );  
}

export default Python;