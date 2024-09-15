const API_URL = 'http://localhost:5000/api';

const apiService = {
  getPersonalizedQuestions: async (generalResponses) => {
    try {
      const response = await fetch(`${API_URL}/personalized-questions`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ responses: generalResponses }),
      });

      if (!response.ok) {
        throw new Error(`Error: ${response.statusText}`);
      }

      // Safely handle JSON parsing
      const data = await response.json();
      return data;
      
    } catch (error) {
      console.error('Error fetching personalized questions:', error);
      throw error;
    }
  },

  getQuizResults: async (personalResponses) => {
    try {
      const response = await fetch(`${API_URL}/quiz-results`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ responses: personalResponses }),
      });

      if (!response.ok) {
        throw new Error(`Error: ${response.statusText}`);
      }

      // Safely handle JSON parsing
      const data = await response.json();
      return data;

    } catch (error) {
      console.error('Error fetching quiz results:', error);
      throw error;
    }
  }
};

export default apiService;
