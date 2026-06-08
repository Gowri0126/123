import React from "react";

function Controls({ onScan, onReset }) {
  return (
    <div className="card controls" style={styles.wrapper}>

      <button
        className="btn btn-primary"
        style={styles.button}
        onClick={() => {
          console.log("SCAN TRIGGERED");
          onScan();
        }}
      >
        🔍 Scan System
      </button>

      <button
        className="btn btn-warning"
        style={styles.button}
        onClick={() => {
          console.log("RESET TRIGGERED");
          onReset();
        }}
      >
        ♻ Reset System
      </button>

    </div>
  );
}

const styles = {
  wrapper: {
    display: "flex",
    gap: "12px",
    marginBottom: "15px",
  },
  button: {
    cursor: "pointer",
    padding: "10px 15px",
    borderRadius: "8px",
    fontWeight: "bold",
  },
};

export default Controls;