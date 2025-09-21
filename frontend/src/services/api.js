import axios from 'axios'

const api = axios.create({ baseURL: process.env.REACT_APP_API_URL || 'http://localhost:8000' })

export async function run(prompt){
  const res = await api.post('/run', { prompt })
  return res.data
}

export default api
