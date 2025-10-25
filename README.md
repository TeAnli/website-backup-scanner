# Website Backup Scanner

A Python script to scan for common website backup files by checking various filename combinations.

## Installation

1. Clone or download this repository
2. Install required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python website_backup_scanner.py <target_url>
```

### Example

```bash
python website_backup_scanner.py https://example.com
```

## What It Scans For

The script checks for the following backup file combinations:

**File Names:**
- web, website, backup, back, www, wwwroot, temp

**File Extensions:**
- tar, tar.gz, zip, rar, 7-zip, 7z


# Note
This tool is intended for legitimate security testing and backup discovery purposes only. Only use on websites you own or have explicit permission to test.
