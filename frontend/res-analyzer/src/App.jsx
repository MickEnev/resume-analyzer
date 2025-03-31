import { useState, useEffect } from 'react'
import ReactMarkdown from 'react-markdown';
import './App.css'

function App() {
  const [currentSkills, setCurrentSkills] = useState(0)
  const [resume, setResume] = useState(null)
  const [jobDesc, setJobDesc] = useState(null)
  const [loading, setLoading] = useState(false)



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

    setLoading(true)

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
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Resume Roaster</h1>
        <div className="btn-container">
          <div className="file-input">
            <label for="resume">Resume: </label>
            <input type="file" onChange={(e) => handleFileChange(e, "resume")} />
          </div>
          <div className="file-input">
            <label for="job-desc">Job Description: </label>
            <input type="file" onChange={(e) => handleFileChange(e, "jobDesc")} />
          </div>
        </div>
        <button className="upload-btn" onClick={handleUpload}>Upload</button>
        <div className="skills-container">
          {loading ? <p>Loading...</p> : currentSkills !== 0 && <ReactMarkdown>{currentSkills}</ReactMarkdown>}
          {/* TODO: Add buttons that let the user further query the LLM. Buttons could include: Next steps, skill match percentage */}
        </div>
      </header>
    </div>
  );
}

export default App
