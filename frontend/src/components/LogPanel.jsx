import React from 'react'

export default function LogPanel({logs}){
  return <pre className="bg-gray-50 p-3">{JSON.stringify(logs, null, 2)}</pre>
}
