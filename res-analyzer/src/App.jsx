import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [currentSkills, setCurrentSkills] = useState(0)

  useEffect(() => {
    fetch('/skills').then(res => res.json()).then(data => {
      setCurrentSkills(data.skills);
    });
  }, []);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
  }

  return (
    <div className="App">
      <header className="App-header">
        <div className="btn-container">
          <div className="res-div">
            <label for="resume">Resume: </label>
            <input type='file' onChange={handleFileChange} name="resume"/>
          </div>
          <div className="job-div">
            <label for="job-desc">Job Description: </label>
            <input type='file' onChange={handleFileChange} name="job-desc"/>
          </div>
        </div>
        
        {currentSkills != 0 && (
          <p>{currentSkills}.</p>
        )}
        
      </header>
    </div>
  );
}

export default App
