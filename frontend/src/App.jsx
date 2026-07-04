import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {

  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [file, setFile] = useState(null);

  const analyzeLogs = async () => {

    if (!file) {
      alert("Please upload a JSON file.");
      return;
    }

    setLoading(true);

    try {

      const text = await file.text();
      const logs = JSON.parse(text);

      const res = await axios.post(
        "https://sentinelai-1-ikqw.onrender.com/analyze",
        logs
);

      setData(res.data);

    } catch (err) {

      console.error(err);

      alert("Invalid JSON or Backend Error.");

    }

    setLoading(false);

  };

  return (

    <div className="app">

      <h1 className="title">
        🛡 SentinelAI SOC Dashboard
      </h1>

      <div className="upload">

        <input
          type="file"
          accept=".json"
          onChange={(e)=>setFile(e.target.files[0])}
        />

        <br/><br/>

        <button onClick={analyzeLogs}>
          {loading ? "Analyzing..." : "Analyze Logs"}
        </button>

      </div>

      {data && (

        <>

          <div className="cards">

            <div className="card">
              <h3>Threat Score</h3>
              <h1>{data.summary.threat_score}</h1>
            </div>

            <div className="card">
              <h3>Severity</h3>
              <h1>{data.summary.severity}</h1>
            </div>

            <div className="card">
              <h3>Confidence</h3>
              <h1>{data.summary.confidence}%</h1>
            </div>

          </div>

          <div className="section">

            <h2>Threat Intelligence</h2>

            <p><strong>Reputation:</strong> {data.threat_intelligence.reputation}</p>

            <p><strong>Country:</strong> {data.threat_intelligence.country}</p>

            <p><strong>Malicious Score:</strong> {data.threat_intelligence.malicious_score}</p>

          </div>

          <div className="section">

            <h2>Recommended Actions</h2>

            <ul>

              {data.recommended_action.map((item,index)=>(
                <li key={index}>{item}</li>
              ))}

            </ul>

          </div>

          <div className="section">

            <h2>Incident Report</h2>

            <pre className="report">

              {data.incident_report}

            </pre>

          </div>

        </>

      )}

    </div>

  );

}

export default App;