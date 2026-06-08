export default function Logs({ logs }) {
  return (
    <div className="bg-gray-900 p-4 rounded-xl mt-4">
      <h2 className="mb-2">Logs</h2>

      {logs && logs.length > 0 ? (
        logs.map((log, i) => (
          <div
            key={i}
            className="border-b border-gray-700 py-1"
          >
            <strong>{log.app_name}</strong> |
            Device: {log.device} |
            Status: {log.status} |
            Time: {log.timestamp}
          </div>
        ))
      ) : (
        <p>No logs available</p>
      )}
    </div>
  );
}