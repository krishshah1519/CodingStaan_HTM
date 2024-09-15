import React, { useState } from 'react';
import GeneralQuestions from './components/GeneralQuestions';
import PersonalQuestions from './components/PersonalQuestions';
import QuizResults from './components/QuizResults';
import TestApiConnection from './components/TestApiConnection'; // Import TestApiConnection
import apiService from './services/apiService';

const App = () => {
  const [generalResponses, setGeneralResponses] = useState([]);
  const [personalQuestions, setPersonalQuestions] = useState([]);
  const [personalResponses, setPersonalResponses] = useState([]);
  const [results, setResults] = useState(null);
  const [step, setStep] = useState(1);
  const [showTest, setShowTest] = useState(false); // State to toggle TestApiConnection

  // Handle submission of general responses
  const handleGeneralResponses = (responses) => {
    setGeneralResponses(responses);
    apiService.getPersonalizedQuestions(responses)
      .then((data) => {
        setPersonalQuestions(data.questions);
        setStep(2);
      })
      .catch((error) => {
        console.error('Error fetching personalized questions:', error);
      });
  };

  // Handle submission of personal responses
  const handlePersonalResponses = (responses) => {
    setPersonalResponses(responses);
    apiService.getQuizResults(responses)
      .then((data) => {
        setResults(data.results);
        setStep(3);
      })
      .catch((error) => {
        console.error('Error fetching quiz results:', error);
      });
  };

  return (
    <div>
      <button onClick={() => setShowTest(!showTest)}>
        {showTest ? 'Hide API Test' : 'Show API Test'}
      </button>

      {showTest && <TestApiConnection />} {/* Conditionally render TestApiConnection */}

      {step === 1 && <GeneralQuestions onSubmit={handleGeneralResponses} />}
      {step === 2 && <PersonalQuestions questions={personalQuestions} onSubmit={handlePersonalResponses} />}
      {step === 3 && <QuizResults results={results} />}
    </div>
  );
};

export default App;
