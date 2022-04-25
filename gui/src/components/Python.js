import React, { useEffect, useState } from "react";
import '../style/Modal.css';
import Wave from "./animations/Wave";

// Top Level component for the modal window that handles the python script
function Python() {
    const { PythonShell } = window.require('python-shell');
    const { ipcRenderer } = window.require('electron');

    const [analyzingState, setAnalyzingState] = useState(true);
    const [samplePath, setSamplePath] = useState('');

    console.log("Background Initialized.");
    console.log(__dirname);
    console.log(__filename);
    // This will be called from main.js
    useEffect( () => {
        ipcRenderer.on('START_SCRIPT', (event, args) => {
            console.log('Python Shell Created...');
            setSamplePath(args.data.samplePath);
            let pyshell = new PythonShell(args.data.scriptPath, {
                pythonPath: 'python3',
                pythonOptions:['-u'], // Gets print results in real time
                args: [args.data.jsonPath]
            });

            pyshell.on('message', function(results) {
                ipcRenderer.send('MESSAGE_FROM_BACKGROUND', { message: results });
            });
            // end the input stream and allow the process to exit
            pyshell.end(function (err,code,signal) {
                if (err) throw err;
                setAnalyzingState(false);
                console.log('The exit code was: ' + code);
                console.log('The exit signal was: ' + signal);
                console.log('finished');
            });
        });

        ipcRenderer.send('MODAL_READY');
    }, []);

    function handleClick() {
        ipcRenderer.send('CLOSE_MODAL');
    }

    return(
        <div className="modal">
            <h1>{analyzingState ? 'Analyzing...' : 'Complete'}</h1>
            {analyzingState && <Wave />}
            {!analyzingState && <h3 className="reportLocation">{samplePath}/reporting/</h3>}
            {!analyzingState && <button className="closeButton" onClick={handleClick}>Close</button>}
        </div>
    );  
}

export default Python;