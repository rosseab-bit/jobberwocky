import "./App.css";
import { useState, useEffect } from "react";
import TextField from "@mui/material/TextField";
import axios from "axios";
function App() {
  const [valueSearch, setValueSearch] = useState("");
  const [dataJobs, setDataJobs] = useState([]);
  const [loading, setLoading] = useState(false);
  const handleSearch = (e) => {
    console.log("value search: ", e.target.value);
    setValueSearch(e.target.value);
  };
  const getDataJobs = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:8000/api/joblist/");
      setDataJobs(response.data);
    } catch (err) {
      console.log("# - error get jobs: ", err);
    }
  };
  useEffect(() => {
    getDataJobs();
  }, []);
  useEffect(() => {
    setLoading(true);
    if (valueSearch.length > 0) {
      let updateData = dataJobs.filter(
        (item) =>
          item.position.toLowerCase().includes(valueSearch.toLowerCase()) ??
          item
      );
      setDataJobs(updateData);
    } else if (valueSearch.length === 0) {
      getDataJobs();
    }
    setLoading(false);
  }, [valueSearch]);
  return (
    <div className="App">
      <div className="form-input">
        <TextField
          id="outlined-basic"
          value={valueSearch}
          onChange={(e) => handleSearch(e)}
          label="Search Position"
          variant="outlined"
        />
      </div>
      <div className="container-cards-section">
        {!loading &&
          dataJobs.map((item) => (
            <div className="card-container">
              <div>
                <span className="titles-card">Pisition: </span>
                {item.position}{" "}
              </div>
              <div>
                <span className="titles-card">Country: </span> {item.country}
              </div>
              <div>
                <span className="titles-card">Skills: </span>
                {item.skills}{" "}
              </div>
              <div>
                <span className="titles-card">WorkType: </span>
                {item.work_type}
              </div>
            </div>
          ))}
      </div>
    </div>
  );
}

export default App;
