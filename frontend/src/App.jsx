import React from 'react'
import PromptBox from './components/PromptBox'

export default function App(){
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Recursive AI Executor (dev)</h1>
      <PromptBox />
    </div>
  )
}
