import React, { useEffect } from 'react';
import apiService from '../services/apiService';  // Adjust the path if needed

const TestApiConnection = () => {
  useEffect(() => {
    // Test getPersonalizedQuestions endpoint
    const testPersonalizedQuestions = async () => {
      try {
        const response = await apiService.getPersonalizedQuestions([1, 2, 3]);
        console.log('Personalized Questions Response:', response);
      } catch (error) {
        console.error('Error testing getPersonalizedQuestions:', error);
      }
    };

    // Test getQuizResults endpoint
    const testQuizResults = async () => {
      try {
        const response = await apiService.getQuizResults(['answer1', 'answer2']);
        console.log('Quiz Results Response:', response);
      } catch (error) {
        console.error('Error testing getQuizResults:', error);
      }
    };

    testPersonalizedQuestions();
    testQuizResults();
  }, []);

  return <div>Testing API Connection...</div>;
};

export default TestApiConnection;
