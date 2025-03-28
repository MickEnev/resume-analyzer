import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [currentSkills, setCurrentSkills] = useState(0)

  useEffect(() => {
    fetch('/skills').then(res => res.json()).then(data => {
      console.log(data)
      setCurrentSkills(data.skills);
    });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <p>{currentSkills}.</p>
      </header>
    </div>
  );
}

export default App
