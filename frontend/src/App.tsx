import { useEffect, useState } from 'react';

function App() {
  const [status, setStatus] = useState<string>('loading');

  useEffect(() => {
    fetch('/api/health')
      .then(res => res.json())
      .then(data => setStatus(`backend: ${data.status}`))
      .catch(() => setStatus('backend: error'));
  }, []);

  return (
    <div className="min-h-screen bg-gray-900 text-white flex flex-col items-center justify-center font-sans">
      <h1 className="text-4xl font-bold mb-4 text-yellow-500">THEMIS</h1>
      <p className="text-lg">Justice in Your Language</p>
      <div className="mt-8 p-4 bg-gray-800 rounded-lg shadow-lg border border-gray-700">
        <span className="font-mono text-green-400">{status}</span>
      </div>
    </div>
  );
}

export default App;
