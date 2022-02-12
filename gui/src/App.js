import './style/App.css';

import MainConatiner from './components/MainContainer';
import AnalysisButton from './components/AnalysisButton';
import FileSearch from './components/FileSearch';

import { useState } from 'react';
const { ipcRenderer } = window.require('electron');

function App() {

  const [filePath, setFilePath] = useState('');
  const [frequencies, setFrequencies] = useState([]);

  function storePath(path) {
    setFilePath(path);
  }

  function storeFrequencies(newFrequencies) {
    setFrequencies(newFrequencies);
  }

  function sendToPython() {

    ipcRenderer.send(
      'PYTHON_START', 
      { 
        "Key1": 123,
        "Key2": 456
      }
    );
  }

  function runAnalysis() {
    console.log(filePath);
    console.log(frequencies);

    sendToPython();
  }

  return (
    <div className="App">
      <FileSearch storePath={storePath}/>
      <MainConatiner storeFrequencies={storeFrequencies}/>
      <AnalysisButton runAnalysis={(runAnalysis)}/>
    </div>
  );
}

export default App;
