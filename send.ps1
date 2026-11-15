# Usage: .\send.ps1 "all your text in one pair of double quotes"
param([string]$Text, [string]$Creator = "saba")

$body = @{ text = $Text; creator_id = $Creator } | ConvertTo-Json
Invoke-RestMethod -Uri "http://127.0.0.1:5000/submit" -Method Post -ContentType "application/json" -Body $body | ConvertTo-Json