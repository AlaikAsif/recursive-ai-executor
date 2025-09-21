import React, {useState} from 'react'
import axios from 'axios'

export default function PromptBox(){
  const [prompt, setPrompt] = useState('')
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)

  const submit = async () => {
    setLoading(true)
    try{
      const res = await axios.post('/api/run', { prompt })
      setResult(res.data)
    }catch(e){
      setResult({ error: e.message })
    }finally{ setLoading(false) }
  }

  return (
    <div>
      <textarea value={prompt} onChange={(e)=>setPrompt(e.target.value)} rows={6} className="w-full p-2 border" />
      <div className="mt-2">
        <button onClick={submit} className="px-4 py-2 bg-blue-600 text-white rounded" disabled={loading}>Run</button>
      </div>
      <pre className="mt-4 bg-gray-100 p-2">{result ? JSON.stringify(result, null, 2) : 'No result yet'}</pre>
    </div>
  )
}
