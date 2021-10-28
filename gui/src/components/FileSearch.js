import { useState } from "react";

import '../style/FileSearch.css';

function FileSearch() {

    const [filePath, setFilePath] = useState('Folder Location...');

    function handleChange(e) {
        console.log(e.target.files[0].path);
        setFilePath(e.target.files[0].path);
    }

    return(
        <div className='File-Search-Container'>

            {/* <input className='Search-Bar' type="file" id="file-upload" name="name" /> */}
            <h3 className='Search-Bar'>{filePath}</h3>
            <div className='File-Search-Button-Container'>
                <label for='files' className='Search-Button'>Select Folder</label>
                <input id='files' type='file' className='File-Search-Button' onChange={handleChange}/>
            </div>
        
        </div>
    );
}

export default FileSearch;