import '../style/MainContainer.css';

import React, {useState} from 'react';
import Frequency from './Frequency';

function MainConatiner() {
    const [input, setInput] = useState('')
    const [formValues, setFormValues] = useState([]);
    const [count, setCount] = useState(0);

    function hanleInput(e) {
        setInput(e.target.value);
    }

    function handleFrequencyRemove(value) {
        console.log(value);
        const tempArr = [...formValues];
        console.log(tempArr)
        tempArr.splice(tempArr.indexOf(value), 1);
        setFormValues(tempArr);
    }

    function handleSubmit() {
        const regex = /^-?[0-9]+.?[0-9]*$/g;
        const formatedInput = input.trim();
        if (formatedInput !== '' && formatedInput.match(regex) !== null) {
            if (!formValues.includes(formatedInput)) {
                console.log(formatedInput);
                setCount(count + 1);
                
                const newFormValues = [formatedInput, ...formValues]
                setFormValues(newFormValues);
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