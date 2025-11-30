# Fixing Cyrillic Character Display in PowerShell

If you see `????` instead of Cyrillic characters when copying file paths in PowerShell, follow these steps:

## Quick Fix (Temporary - Current Session Only)

Run these commands in your PowerShell session:

```powershell
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
[Console]::InputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8
chcp 65001
```

## Permanent Fix

### Option 1: Use the Provided Script (Recommended)

Run the PowerShell configuration script:

```powershell
.\fix_powershell_encoding.ps1
```

Then restart PowerShell or reload your profile:

```powershell
. $PROFILE
```

### Option 2: Manual Configuration

1. Open PowerShell and check if you have a profile:
   ```powershell
   Test-Path $PROFILE
   ```

2. If it returns `False`, create the profile directory:
   ```powershell
   New-Item -ItemType Directory -Path (Split-Path -Parent $PROFILE) -Force
   ```

3. Edit your PowerShell profile:
   ```powershell
   notepad $PROFILE
   ```

4. Add these lines to the profile:
   ```powershell
   # Set UTF-8 encoding for console (fixes Cyrillic character display)
   [Console]::OutputEncoding = [System.Text.Encoding]::UTF8
   [Console]::InputEncoding = [System.Text.Encoding]::UTF8
   $OutputEncoding = [System.Text.Encoding]::UTF8
   chcp 65001 | Out-Null
   ```

5. Save and close Notepad, then reload the profile:
   ```powershell
   . $PROFILE
   ```

## Alternative: Use Windows Terminal

Windows Terminal (available from Microsoft Store) has better UTF-8 support by default. Consider using it instead of the default PowerShell console.

## Testing

After applying the fix, try copying a file path with Cyrillic characters. You should see the characters correctly instead of `????`.

Example:
```powershell
"F:\WORK\_Личные Проекты\Учёба СПБГИК\..."
```

## Notes

- The Python script (`assemblyai_transcriber.py`) has been updated to handle UTF-8 encoding automatically
- This fix applies to PowerShell console encoding only
- You may need to restart your terminal/IDE after applying the fix



