import React, { useState, useEffect } from "react";

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/data')
      .then((response) => response.json())
      .then((data) => setData(data.message))
      .catch((error) => console.error(error));
  }, []);

  return (
    <div className="App">
      <h1>{data ? data : "Loading..."}</h1>
    </div>
  );
}

export default App;
