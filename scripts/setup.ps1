<#
.SYNOPSIS
    Downloads typst binary for the current platform.
.DESCRIPTION
    Fetches the latest typst release from GitHub and extracts the binary
    to the project root. Skips if typst is already available.
#>
param(
    [string]$Version = "0.14.2"
)

$ErrorActionPreference = "Stop"

function Test-Typst {
    try {
        $result = & typst --version 2>&1
        if ($LASTEXITCODE -eq 0) { return $true }
    } catch {}
    if (Test-Path "./typst.exe") { return $true }
    if (Test-Path "./typst") { return $true }
    return $false
}

if (Test-Typst) {
    Write-Host "typst already available." -ForegroundColor Green
    try { & typst --version 2>$null } catch { & ./typst.exe --version 2>$null }
    exit 0
}

$os = if ($IsLinux) { "unknown-linux" } elseif ($IsMacOS) { "apple-darwin" } else { "pc-windows-msvc" }
$arch = if ([System.Runtime.InteropServices.RuntimeInformation]::OSArchitecture -eq "Arm64") { "aarch64" } else { "x86_64" }
$ext = ".zip"
$binExt = if ($os -eq "pc-windows-msvc") { ".exe" } else { "" }

$fileName = "typst-$arch-$os$ext"
$url = "https://github.com/typst/typst/releases/download/v$Version/$fileName"

Write-Host "Downloading typst v$Version for $os-$arch..." -ForegroundColor Cyan
Write-Host "URL: $url"

$tmpDir = [System.IO.Path]::GetTempPath() + "aerocv-setup"
if (Test-Path $tmpDir) { Remove-Item -Recurse -Force $tmpDir }
New-Item -ItemType Directory -Path $tmpDir -Force | Out-Null

$archivePath = Join-Path $tmpDir $fileName
Invoke-WebRequest -Uri $url -OutFile $archivePath -UseBasicParsing

Write-Host "Extracting..." -ForegroundColor Cyan

if ($os -eq "pc-windows-msvc") {
    Expand-Archive -Path $archivePath -DestinationPath $tmpDir -Force
    $typstBin = Get-ChildItem -Path $tmpDir -Recurse -Filter "typst.exe" | Select-Object -First 1
} else {
    & tar -xf $archivePath -C $tmpDir 2>$null
    $typstBin = Get-ChildItem -Path $tmpDir -Recurse -Filter "typst" -File | Select-Object -First 1
}

if (-not $typstBin) {
    Write-Host "ERROR: typst binary not found in archive" -ForegroundColor Red
    exit 1
}

Copy-Item $typstBin.FullName -Destination ".\typst$binExt" -Force
if ($os -ne "pc-windows-msvc") {
    & chmod +x "./typst"
}

Remove-Item -Recurse -Force $tmpDir

Write-Host ""
Write-Host "typst v$Version installed successfully." -ForegroundColor Green
& ".\typst$binExt" --version
