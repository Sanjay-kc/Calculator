import './App.css';
import Wrapper from "./components/Wrapper";
import Screen from "./components/Screen";
import ButtonBox from "./components/ButtonBox";
import Button from "./components/Button";
import React, { useState } from 'react';
import * as math from 'mathjs';

const btnValues = [
  ["C", "(", ")", ".", "+","-", "*", "/"],
  [1, 2, 3, 4, 5, 6, 7, 8, 9, 0,'Del', "="],
];

function App() {
  const [inputValue,setinputValue] = useState("");
  const [steps, setSteps] = useState([]);
  const [R,setR] = useState('')
  const [showSteps, setShowSteps] = useState(false);

  const postToSrv = async(value) =>{
    const response = await fetch('http://127.0.0.1:5000',{
      method : 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({expression: value}),
  });
  if (response.ok) {  // Check if the request was successful
    const data = await response.json();  // Parse the response as JSON
    console.log(data);
    return data;
      // Log the parsed data
  } else {
    return "Error!"
    // console.log('Server responded with status', response.status);
  }
  
  }
  return (
    <Wrapper>
      {/* <div className='tagline' style={{fontFamily:'Papyurs'}}> */}
      {/* <h1>Math your way to future!!</h1></div> */}
      <Screen value={inputValue||0} />
      <ButtonBox>
        {
          btnValues.flat().map((btn, i) => {
            return (
              <Button
                key={i}
                className={btn === "=" || btn === "Del"? "equals" : ""}
                value={btn}
                onClick={() => {
                  if (btn ==="C"){
                    setinputValue("");
                    setSteps([]);
                    setR('');
                    setShowSteps(false);
                  } else if (btn ==="="){
                    postToSrv(inputValue).then((data) => {
                      setR(inputValue);
                      setinputValue(data.result);
                      setSteps(data.steps);
                      // setR(data.R);
                      setShowSteps(true);
                    }

                  );
                  } else if (btn ==="Del"){
                    setinputValue(prevValue => prevValue.slice(0, -1));
                  } else {
                    setinputValue(prevValue => prevValue + btn.toString());
                  }
                }}
              />
            );
          })
        }
      </ButtonBox>
      {showSteps && 
        <div>
          <h2>Expression</h2>
          <p>{R}</p>
          <h2>Steps</h2>
          <ul>
            {
              steps.map((step, i) => {
                return (
                  <li key={i}>Step {i+1} : {step} = {math.evaluate(step)}</li>
                );
              })
            }
          </ul>
        </div>
      }
    </Wrapper>
  );
}

export default App;
