import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:5000"
});

// Scan system
export const scanApps = () => API.get("/scan");

// Fetch logs
export const fetchLogs = () => API.get("/logs");

// Block application
export const blockApp = (app) => API.post("/block", app);

// Reset system
export const resetSystem = () => API.post("/reset");