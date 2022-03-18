import React from "react";
import "../style/ValueContainer.css";
function ValueContainer(props) {

    function storeInput(event) {
        const payload = {
            'pH': props.value, 
            'frequency': event.target.value, 
            'index': props.indexValue
        };
        props.storeData(payload);
        // console.log(payload);
    }

    return(
        <div className='Value-Container'>
            <div className="PH-Container">
                <p>{props.value}</p>
            </div>
            <div className="PH-Input-Container">
                <input placeholder={props.value} onInput={storeInput}/>
            </div>

        </div>
    );
}

export default ValueContainer;