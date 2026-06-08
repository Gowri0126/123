export default function AppTable({ apps, onBlock }) {

  const getCamStatus = (app) => {
    return app.webcam === 1 ? "dot-camera" : "dot-safe";
  };

  const getMicStatus = (app) => {
    return app.mic === 1 ? "dot-mic" : "dot-safe";
  };

  return (
    <div className="card">
      <h3>Active Applications</h3>

      {apps.length > 0 ? (
        apps.map((app, i) => (
          <div className="row" key={i}>

            <span>{app.name}</span>

            {/* CAMERA */}
            <span>
              📷 <span className={getCamStatus(app)}></span>
            </span>

            {/* MICROPHONE */}
            <span>
              🎤 <span className={getMicStatus(app)}></span>
            </span>

            <button
              className="btn btn-danger"
              onClick={() => onBlock(app)}
            >
              Block
            </button>

          </div>
        ))
      ) : (
        <p>No applications detected</p>
      )}

    </div>
  );
}