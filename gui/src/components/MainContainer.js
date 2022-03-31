import '../style/MainContainer.css';

import React, {useState} from 'react';
import ValueContainer from './ValueContainer';
const { ipcRenderer } = window.require('electron');

function MainConatiner(props) {
    const [phValues, setPhValues] = useState([]);
    
    // Return of Folder structure from Main.js
    ipcRenderer.on('PH_VALUES_RETURN', (event, args) => {
        setPhValues(args);
        props.setPhCount(args.length);
    });

    return(
        <div className='Main-Container'>

            <h1 className='Container-Title'>Frequencies</h1>

            <div className='Frequency-Container'>
                <div className='Header-Container'>
                    <h2>pH</h2>
                    <h2>Frequencies</h2>

                </div>
                <div>
                    {phValues.map((value, i) => <ValueContainer value={value} indexValue={i} storeData={props.storeData}/>)}
                </div>

            </div>

        </div>
    );
}

export default MainConatiner;