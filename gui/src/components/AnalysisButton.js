import React from "react";

function AnalysisButton(props) {
    return(
        <div className='Analysis-Button-Container'>
            <button className='Analysis-Button' onClick={props.runAnalysis}>Analysis</button>
        </div>        
    );
}


export default AnalysisButton;