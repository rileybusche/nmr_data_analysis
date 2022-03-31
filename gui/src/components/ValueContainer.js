import React, { useState } from "react";
import "../style/ValueContainer.css";
function ValueContainer(props) {

    const [inputState, setInputState] = useState(true);
    
    const re = /^-?[0-9]?[.]?[0-9]+$/g;

    const storeInput = (event) => {
        // Checks if input field is a valid input
        const frequencies = event.target.value.split(' ');
        frequencies.every(frequency => {
            if (frequency.search(re)){
                setInputState(false);
                // Exits loop if invalid input
                return false;
            } else {
                setInputState(true);
                return true;
            }
        });
        
        // If input field is valid, store data
        console.log('InputState ', inputState);
        console.log(event.target.value)
        const payload = {
            'pH': props.value, 
            'frequency': event.target.value, 
            'index': props.indexValue
        };
        props.storeData(payload);
    }

    return(
        <div className='Value-Container'>
            <div className="PH-Container">
                <p>{props.value}</p>
            </div>
            <div className="PH-Input-Container">
                <input className={inputState ? 'Input-Valid' : 'Input-Invalid'} placeholder={props.value} onInput={storeInput}/>
            </div>

        </div>
    );
}

export default ValueContainer;