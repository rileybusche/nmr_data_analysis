import React from "react";

function Frequency(props) {

    return(
        <div className='Frequency-Module'>
            <h3>{props.value}</h3>
            <button onClick={() => props.handleFrequencyRemove(props.value)}>X</button>
        </div>
    );
}

export default Frequency;