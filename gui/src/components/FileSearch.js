import { useState } from "react";

import '../style/FileSearch.css';

function FileSearch(props) {

    const [filePath, setFilePath] = useState('Path to Difframp file...');

    function handleChange(e) {
        setFilePath(e.target.files[0].path);
        props.storePath(e.target.files[0].path);
    }

    return(
        <div className='File-Search-Container'>

            {/* <input className='Search-Bar' type="file" id="file-upload" name="name" /> */}
            <h4 className='Search-Bar'>{filePath}</h4>
            <div className='File-Search-Button-Container'>
                <label for='files' className='Search-Button'>Select File</label>
                <input id='files' type='file' className='File-Search-Button' onChange={handleChange}/>
            </div>
        
        </div>
    );
}

export default FileSearch;