import '../style/MainContainer.css';

import React, {useState} from 'react';
import Frequency from './Frequency';

function MainConatiner(props) {
    const [input, setInput] = useState('')
    const [formValues, setFormValues] = useState([]);

    function hanleInput(e) {
        setInput(e.target.value);
    }

    function handleFrequencyRemove(value) {

        const tempArr = [...formValues];

        tempArr.splice(tempArr.indexOf(value), 1);
        setFormValues(tempArr);
        props.storeFrequencies(tempArr);
    }

    function handleSubmit() {
        const regex = /^-?[0-9]+.?[0-9]*$/g;
        const formatedInput = input.trim();
        if (formatedInput !== '' && formatedInput.match(regex) !== null) {
            if (!formValues.includes(formatedInput)) {

                const newFormValues = [formatedInput, ...formValues]
                setFormValues(newFormValues);

                props.storeFrequencies(newFormValues);
            }
        }
    }

    return(
        <div className='Main-Container'>

            <h1 className='Container-Title'>Frequencies</h1>

            <div className='Frequency-Container'>
                <div className='Input-Container'>
                    <input className='Frequency-Input' value={input} onInput={hanleInput} id="Frequency-Input" name="name" />
                    <button onClick={handleSubmit}>Add</button>
                </div>
                <div className='Module-Container'>
                    { formValues.map((value, i) => <Frequency value={value} handleFrequencyRemove={handleFrequencyRemove} key={i} />) }
                </div>
            </div>

        </div>
    );
}

export default MainConatiner;