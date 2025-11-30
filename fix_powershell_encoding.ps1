# PowerShell script to fix UTF-8 encoding for Cyrillic characters
# Run this script once to configure your PowerShell profile

Write-Host "Configuring PowerShell for UTF-8 encoding..." -ForegroundColor Green

# Get the PowerShell profile path
$profilePath = $PROFILE.CurrentUserAllHosts

# Create profile directory if it doesn't exist
$profileDir = Split-Path -Parent $profilePath
if (-not (Test-Path $profileDir)) {
    New-Item -ItemType Directory -Path $profileDir -Force | Out-Null
}

# UTF-8 configuration commands
$utf8Config = @"

# Set UTF-8 encoding for console (fixes Cyrillic character display)
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
[Console]::InputEncoding = [System.Text.Encoding]::UTF8
`$OutputEncoding = [System.Text.Encoding]::UTF8
chcp 65001 | Out-Null

"@

# Check if configuration already exists
if (Test-Path $profilePath) {
    $existingContent = Get-Content $profilePath -Raw
    if ($existingContent -match "UTF8|UTF-8|chcp 65001") {
        Write-Host "UTF-8 configuration already exists in profile." -ForegroundColor Yellow
        Write-Host "Profile location: $profilePath" -ForegroundColor Cyan
    } else {
        # Append to existing profile
        Add-Content -Path $profilePath -Value $utf8Config
        Write-Host "UTF-8 configuration added to existing profile." -ForegroundColor Green
        Write-Host "Profile location: $profilePath" -ForegroundColor Cyan
    }
} else {
    # Create new profile with UTF-8 configuration
    Set-Content -Path $profilePath -Value $utf8Config
    Write-Host "New PowerShell profile created with UTF-8 configuration." -ForegroundColor Green
    Write-Host "Profile location: $profilePath" -ForegroundColor Cyan
}

Write-Host "`nConfiguration complete!" -ForegroundColor Green
Write-Host "Please restart PowerShell or run: . `$PROFILE" -ForegroundColor Yellow
Write-Host "`nTo test, try copying a file path with Cyrillic characters." -ForegroundColor Cyan



