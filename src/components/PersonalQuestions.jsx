import React, { useState } from 'react';

const PersonalQuestions = ({ questions, onSubmit }) => {
  // Initialize responses with an empty string for each question
  const [responses, setResponses] = useState(Array(questions.length).fill(''));

  const handleInputChange = (index, value) => {
    const updatedResponses = responses.map((response, i) => 
      i === index ? value : response
    );
    setResponses(updatedResponses);
  };

  const handleSubmit = () => {
    // Optionally add validation to ensure all responses are filled
    if (responses.includes('')) {
      alert('Please answer all questions before submitting.');
      return;
    }
    onSubmit(responses);
  };

  return (
    <div>
      {questions.map((question, index) => (
        <div key={index}>
          <label>{question}</label>
          <input
            type="text"
            value={responses[index]}  // Controlled input
            onChange={(e) => handleInputChange(index, e.target.value)}  // Update state on change
          />
        </div>
      ))}
      <button onClick={handleSubmit}>Submit</button>
    </div>
  );
};

export default PersonalQuestions;
