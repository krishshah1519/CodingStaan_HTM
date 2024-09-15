import React, { useState } from 'react';

const GeneralQuestions = ({ onSubmit }) => {
  // Define your questions and the type of input they should have
  const questions = [
    { text: 'What is your age?', type: 'age' }, // Slider from 1 to 100
    { text: 'What is your highest level of education?', type: 'text' },
    { text: 'What is your current employment status?', type: 'text' },
    { text: 'How satisfied are you with your current job?', type: 'rating' }, // Rating from 1 to 10
    { text: 'How many years of experience do you have in your field?', type: 'experience' }, // Slider from less than a year to 50+
    { text: 'How confident are you in achieving your career goals?', type: 'rating' } // Rating from 1 to 10
  ];

  const [responses, setResponses] = useState(questions.map((q) => (q.type === 'rating' ? 5 : q.type === 'age' ? 25 : q.type === 'experience' ? 1 : '')));

  const handleResponseChange = (index, value) => {
    const updatedResponses = responses.map((response, i) => 
      i === index ? value : response
    );
    setResponses(updatedResponses);
  };

  const handleSubmit = () => {
    onSubmit(responses);
  };

  return (
    <div>
      <h2>General Questions</h2>
      {questions.map((question, index) => (
        <div key={index}>
          <label>{question.text}</label>
          {question.type === 'text' ? (
            <input
              type="text"
              value={responses[index]}
              onChange={(e) => handleResponseChange(index, e.target.value)}
            />
          ) : question.type === 'age' ? (
            <div>
              <input
                type="range"
                min="1"
                max="100"
                value={responses[index]}
                onChange={(e) => handleResponseChange(index, e.target.value)}
              />
              <span>{responses[index]} years</span>
            </div>
          ) : question.type === 'experience' ? (
            <div>
              <input
                type="range"
                min="0"
                max="51"
                value={responses[index]}
                onChange={(e) => handleResponseChange(index, e.target.value)}
              />
              <span>
                {responses[index] === '0'
                  ? 'Less than a year'
                  : responses[index] === '51'
                  ? '50+ years'
                  : `${responses[index]} years`}
              </span>
            </div>
          ) : (
            <select
              value={responses[index]}
              onChange={(e) => handleResponseChange(index, e.target.value)}
            >
              {Array.from({ length: 10 }, (_, i) => i + 1).map((num) => (
                <option key={num} value={num}>
                  {num}
                </option>
              ))}
            </select>
          )}
        </div>
      ))}
      <button onClick={handleSubmit}>Submit</button>
    </div>
  );
};

export default GeneralQuestions;
