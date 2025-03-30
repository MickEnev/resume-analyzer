import { useState, useEffect } from 'react'
import ReactMarkdown from 'react-markdown';
import './App.css'

function App() {
  const [currentSkills, setCurrentSkills] = useState(0)
  const [resume, setResume] = useState(null)
  const [jobDesc, setJobDesc] = useState(null)



  const handleFileChange = (event, type) => {
    if (type === "resume") {
      setResume(event.target.files[0]);
    } else if (type === "jobDesc") {
      setJobDesc(event.target.files[0]);
    }
  };

  const handleUpload = async() => {
    if (!resume || !jobDesc) {
      console.error("Both files are required.")
      return;
    }

    const formData = new FormData();
    formData.append("resume", resume);
    formData.append("job_description", jobDesc);

    try {
      const response = await fetch("/skills", {
        method: "POST",
        body: formData,
      });
      
      const result = await response.json();
      setCurrentSkills(result.skills);
      console.log("Upload success:", result)
    } catch (error) {
      console.error("Upload error:", error);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <div className="btn-container">
          <div className="res-div">
            <label for="resume">Resume: </label>
            <input type="file" onChange={(e) => handleFileChange(e, "resume")} />
          </div>
          <div className="job-div">
            <label for="job-desc">Job Description: </label>
            <input type="file" onChange={(e) => handleFileChange(e, "jobDesc")} />
          </div>
        </div>
        <button onClick={handleUpload}>Upload</button>
        
        {currentSkills != 0 && (
          <ReactMarkdown>{currentSkills}</ReactMarkdown>
        )}
        
      </header>
    </div>
  );
}

export default App
