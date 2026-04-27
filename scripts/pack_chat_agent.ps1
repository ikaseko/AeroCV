<#
.SYNOPSIS
    Packs AeroCV assets into a ZIP for chat/cloud GPT agents.
.DESCRIPTION
    Builds chat_agent_output/aerocv-chat-agent.zip containing:
    - typst binary (from PATH or local)
    - metadata.md (template catalog for GPT)
    - previews.zip (PNG previews)
    - <template-id>.zip per template (flat, self-contained with fonts + packages)
.NOTES
    Run from project root. Requires Python 3 for pack_per_template.py.
#>

param(
    [string]$TypstPath = "",
    [string]$OutputDir = "chat_agent_output"
)

$ErrorActionPreference = "Stop"
if ($PSScriptRoot) { $Root = Resolve-Path (Join-Path $PSScriptRoot "..") } else { $Root = Get-Location }

Write-Host "=== AeroCV Chat Agent Packager ===" -ForegroundColor Cyan

# Step 1: Find typst binary
if ($TypstPath -and (Test-Path $TypstPath)) {
    $typst = Resolve-Path $TypstPath
} elseif (Test-Path "$Root\typst.exe") {
    $typst = Resolve-Path "$Root\typst.exe"
} elseif (Test-Path "$Root\typst") {
    $typst = Resolve-Path "$Root\typst"
} elseif (Get-Command typst -ErrorAction SilentlyContinue) {
    $typst = (Get-Command typst).Source
} else {
    Write-Host "ERROR: typst binary not found." -ForegroundColor Red
    Write-Host "Install from https://github.com/typst/typst/releases or pass -TypstPath" -ForegroundColor Yellow
    exit 1
}
Write-Host "Using typst: $typst"

# Step 2: Rebuild agent_output/ with updated Python script
Write-Host "`n--- Running pack_per_template.py ---" -ForegroundColor Yellow
python "$Root\scripts\pack_per_template.py"
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: pack_per_template.py failed" -ForegroundColor Red
    exit 1
}

# Step 3: Create output directory
$outPath = Join-Path $Root $OutputDir
if (Test-Path $outPath) { Remove-Item -Recurse -Force $outPath }
New-Item -ItemType Directory -Path $outPath -Force | Out-Null

# Step 4: Build the combined zip
$zipPath = Join-Path $outPath "aerocv-chat-agent.zip"
Write-Host "`n--- Building aerocv-chat-agent.zip ---" -ForegroundColor Yellow

Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem

$zip = [System.IO.Compression.ZipFile]::Open($zipPath, "Create")

function Add-FileToZip($filePath, $entryName) {
    if (Test-Path $filePath) {
        $src = [System.IO.File]::OpenRead((Resolve-Path $filePath).Path)
        $entry = $zip.CreateEntry($entryName, [System.IO.Compression.CompressionLevel]::Optimal)
        $dst = $entry.Open()
        $src.CopyTo($dst)
        $dst.Close()
        $src.Close()
        Write-Host "  + $entryName"
    } else {
        Write-Host "  SKIP $entryName (not found)" -ForegroundColor DarkGray
    }
}

function Add-DirToZip($dirPath, $prefix) {
    if (-not (Test-Path $dirPath)) { return }
    Get-ChildItem $dirPath -Recurse -File | ForEach-Object {
        $rel = $_.FullName.Substring((Resolve-Path $dirPath).Path.Length + 1)
        $entryName = "$prefix/$rel" -replace "\\", "/"
        Add-FileToZip $_.FullName $entryName
    }
}

# Add typst binary
Add-FileToZip $typst "typst"

# Add all files from agent_output/
$agentOutput = Join-Path $Root "agent_output"
if (Test-Path $agentOutput) {
    Get-ChildItem $agentOutput -File | ForEach-Object {
        Add-FileToZip $_.FullName $_.Name
    }
}

# Add SYSTEM_PROMPT_TYPST.md as system_prompt.md
Add-FileToZip "$Root\SYSTEM_PROMPT_TYPST.md" "system_prompt.md"

$zip.Dispose()

$sizeMB = [math]::Round((Get-Item $zipPath).Length / 1MB, 1)
Write-Host "`nDone: $zipPath ($sizeMB MB)" -ForegroundColor Green
