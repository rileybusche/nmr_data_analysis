import './style/App.css';

import MainConatiner from './components/MainContainer';
import AnalysisButton from './components/AnalysisButton';
import FileSearch from './components/FileSearch';

import { useState } from 'react';
const { ipcRenderer } = window.require('electron');

function App() {

  const [filePath, setFilePath] = useState('');
  const [phCount, setPhCount] = useState('');
  // const [frequencies, setFrequencies] = useState([]);
  // const [phList, setPhList] = useState([]);

  var phList = [];
  var frequencyList = [];

  function storePath(path) {
    setFilePath(path);
    // Sends input path to main thread to get file structue to populate pH Values in MainContainer
    ipcRenderer.send(
      'READ_FILES',
      path
    );
  }

  // Data passed back from ValueContainer as Obj.
  function storeData(data) {
    // Should probably be using state some how.... but this works --- Likely a better way to handle this
    phList[data.index] = data.pH;
    frequencyList[data.index] = data.frequency;
    console.log(phList);
    console.log(frequencyList);
    
  }

  function sendToPython() {
    // const payload = [filePath, frequencyList, phList]
    const payload = {
      "SamplesFilePath"  : filePath,
      "Samples"        : {}
    }

    phList.forEach((ph, index) => {
      payload['Samples'][ph] = frequencyList[index];
    });

    console.log(payload);

    // Calls back to main.js to start python process
    // Send Payload to be written to data.json
    ipcRenderer.send(
      'START_BACKGROUND_VIA_MAIN',
      payload
    );
  }

  function runAnalysis() {
    // Make sure the size of the arrays are 1:1 with number of pH Folders
    if (phList.length === phCount && frequencyList.length === phCount) {

      console.log(filePath);
      // console.log(frequencies);

      sendToPython();
    }
  }

  return (
    <div className="App">
      <FileSearch storePath={storePath}/>
      <MainConatiner setPhCount={setPhCount} storeData={storeData}/>
      <AnalysisButton runAnalysis={(runAnalysis)}/>
    </div>
  );
}

export default App;
