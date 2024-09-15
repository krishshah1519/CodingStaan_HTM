import React, { useState } from 'react';

const PersonalQuestions = ({ questions, onSubmit }) => {
  const [responses, setResponses] = useState([]);

  const handleSubmit = () => {
    onSubmit(responses);
  };

  return (
    <div>
      {questions.map((question, index) => (
        <div key={index}>
          <label>{question}</label>
          <input
            type="text"
            onChange={(e) => {
              const newResponses = [...responses];
              newResponses[index] = e.target.value;
              setResponses(newResponses);
            }}
          />
        </div>
      ))}
      <button onClick={handleSubmit}>Submit</button>
    </div>
  );
};

export default PersonalQuestions;
