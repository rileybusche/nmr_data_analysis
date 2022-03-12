import React from "react";
import "../style/ValueContainer.css";
function ValueContainer(props) {

    function StoreInput(event) {
        console.log(event.target.value);
    }

    return(
        <div className='Value-Container'>
            <div className="PH-Container">
                <p>{props.value}</p>
            </div>
            <div className="PH-Input-Container">
                <input placeholder={props.value} onInput={StoreInput}/>
            </div>

        </div>
    );
}

export default ValueContainer;