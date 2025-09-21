import React from 'react'

export default function CodeViewer({code}){
  return <pre className="bg-black text-white p-3 overflow-auto">{code}</pre>
}
