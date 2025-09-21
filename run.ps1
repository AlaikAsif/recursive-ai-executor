# PowerShell helper to start backend and frontend (dev)
Write-Host "Starting backend and frontend (dev)"
# Start backend
Start-Process -NoNewWindow -FilePath pwsh -ArgumentList "-c uvicorn backend.app.main:app --reload --port 8000" 
# Start frontend (assumes npm installed)
Start-Process -NoNewWindow -FilePath pwsh -ArgumentList "-c cd frontend; npm run dev"
