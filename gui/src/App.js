import './style/App.css';

import MainConatiner from './components/MainContainer';
import AnalysisButton from './components/AnalysisButton';
import FileSearch from './components/FileSearch';

function App() {

  return (
    <div className="App">
      <FileSearch />
      <MainConatiner />
      <AnalysisButton />
    </div>
  );
}

export default App;
