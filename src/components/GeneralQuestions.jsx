import React, { useState } from 'react';

const GeneralQuestions = ({ onSubmit }) => {
  // Define your questions
  const questions = [
    'What is your age?',
    'What is your highest level of education?',
    'What is your current employment status?',
    'What are your career goals?',
    'How many years of experience do you have in your field?'
  ];

  const [responses, setResponses] = useState(new Array(questions.length).fill(''));

  const handleResponseChange = (index, value) => {
    const newResponses = [...responses];
    newResponses[index] = value;
    setResponses(newResponses);
  };

  const handleSubmit = () => {
    onSubmit(responses);
  };

  return (
    <div>
      <h2>General Questions</h2>
      {questions.map((question, index) => (
        <div key={index}>
          <label>{question}</label>
          <input
            type="text"
            value={responses[index]}
            onChange={(e) => handleResponseChange(index, e.target.value)}
          />
        </div>
      ))}
      <button onClick={handleSubmit}>Submit</button>
    </div>
  );
};

export default GeneralQuestions;
