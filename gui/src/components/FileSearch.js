import { useState } from "react";

function FileSearch() {
    return(
        <div className='File-Search-Container'>

            {/* <input className='Search-Bar' type="file" id="file-upload" name="name" /> */}
            <h2 className='Search-Bar'>File Location Place Holder</h2>
            <div className='File-Search-Button-Container'>
                <label for='files' className='Search-Button'>Select Folder</label>
                <input id='files' type='file' className='File-Search-Button'/>
            </div>
        
        </div>
    );
}

export default FileSearch;