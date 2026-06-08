import React, { useEffect, useState, useCallback } from "react";
import axios from "axios";

import Header from "./components/Header";
import Controls from "./components/Controls";
import AppTable from "./components/AppTable";
import Logs from "./components/Logs";

function Dashboard() {
  const [apps, setApps] = useState([]);
  const [logs, setLogs] = useState([]);

  const fetchLogs = useCallback(async () => {
    try {
      const res = await axios.get("http://127.0.0.1:5000/logs");
      setLogs(res.data || []);
    } catch (err) {
      console.error(err);
    }
  }, []);

  const blockApp = useCallback(async (app) => {
    try {
      await axios.post("http://127.0.0.1:5000/block", app);
      alert(`${app.name} blocked`);
      fetchLogs();
    } catch (err) {
      console.error(err);
    }
  }, [fetchLogs]);

  const reset = useCallback(async () => {
    try {
      await axios.post("http://127.0.0.1:5000/reset");
      alert("All apps unblocked");
      fetchLogs();
    } catch (err) {
      console.error(err);
    }
  }, [fetchLogs]);

  const refreshDashboard = () => {
    setApps([]);
    setLogs([]);
  };

  const scanApps = useCallback(async () => {
    try {
      console.log("SCANNING...");

      const res = await axios.get("http://127.0.0.1:5000/scan");

      const data = res.data || [];

      console.log("SCAN RESULT:", data);

      setApps(data);

      fetchLogs();

    } catch (err) {
      console.error("SCAN ERROR:", err);
    }
  }, [fetchLogs]);

  useEffect(() => {
    scanApps();

    const interval = setInterval(scanApps, 4000);

    return () => clearInterval(interval);
  }, [scanApps]);

  return (
    <div className="dashboard">

      <Header />

      <Controls
        onScan={scanApps}
        onReset={reset}
      />

      <div className="card">
        <button
          className="btn btn-danger"
          onClick={refreshDashboard}
        >
          Refresh Dashboard
        </button>
      </div>

      <AppTable
        apps={apps}
        onBlock={blockApp}
      />

      <Logs logs={logs} />

    </div>
  );
}

export default Dashboard;