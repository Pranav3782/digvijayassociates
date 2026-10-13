# Digvijay Associates - Local Website Mirror & Server

This repository contains the complete offline clone of [Digvijay Associates](https://www.digvijayassociates.com/), including all pages, services, calculators, forms, utilities, bulletins, stylesheets, and images.

---

## 🚀 How to Run Locally

### Option 1: One-Click Startup (Recommended for Windows)
Simply double-click the **`start_server.bat`** file in this folder.
- It starts the local server.
- It automatically opens [http://localhost:8000](http://localhost:8000) in your default web browser.

---

### Option 2: Run with Custom Python Server
Run the provided `serve.py` script:
```bash
python serve.py
```
Then open your browser and navigate to:
👉 **[http://localhost:8000](http://localhost:8000)**

> **Why `serve.py` is recommended:**
> The original website uses ASP.NET (`.aspx` routes). Python's default `http.server` does not know `.aspx` MIME types and may attempt to download `.aspx` pages as binary files instead of displaying them. `serve.py` maps `.aspx` and `.aspx.html` to `text/html` and seamlessly handles URL routing and CORS headers.

---

### Option 3: Standard Python HTTP Server (Claude's Command)
If you prefer running the standard Python server directly inside the cloned website folder:
```powershell
cd www.digvijayassociates.com
python -m http.server 8000
```
Then visit:
👉 **[http://localhost:8000](http://localhost:8000)**

---

## 📁 Folder Structure

```text
website/
│
├── start_server.bat             # 1-Click launcher for Windows
├── serve.py                     # Custom Python HTTP server with ASPX support
├── README.md                    # Documentation & guide
│
└── www.digvijayassociates.com/  # Root website folder
    ├── index.html               # Main homepage
    ├── image/                   # Logos, banners, icons, and illustrations
    ├── usercss/                 # Site styling and CSS files
    ├── resource/                # Main service pages & company information
    │   ├── Franchise.aspx.html
    │   ├── home.aspx.html
    │   └── Services/            # Accounting, GST, Income Tax, Payroll, etc.
    │       ├── Accounting_Bookkeeping.aspx.html
    │       ├── Company_Registration.aspx.html
    │       ├── Income_Tax.aspx.html
    │       ├── GST.aspx.html
    │       ├── Payroll.aspx.html
    │       └── ...
    │
    ├── resources/               # Tools, Calculators, Bulletins & Forms
    │   ├── Calculators/         # Tax, GST, HRA, EMI, Loan calculators
    │   ├── Forms/               # GST, ROC, Income Tax, FEMA forms
    │   ├── Bulletins/           # Legal, Tax, and Corporate bulletins
    │   ├── Utilities/           # TDS rates, IFSC, Depreciation tables, etc.
    │   └── Links/               # Ease of Doing Business, VAT, Important links
    │
    └── notificationsearch/      # Notifications and circulars archive
```

---

## 🛠️ Note on Claude's Original Command on Windows

Claude suggested running:
```bash
wget --mirror --convert-links --adjust-extension --page-requisites --no-parent https://www.digvijayassociates.com/
```
On **Windows PowerShell**, `wget` is a built-in alias for `Invoke-WebRequest`, which does not recognize GNU `wget` parameters like `--mirror` or `--convert-links`. 

To solve this:
1. Real GNU `wget` (v1.21.4) was installed using `winget install JernejSimoncic.Wget`.
2. The entire site was mirrored using the exact flags, preserving the full directory structure, resources, and internal link conversions.

# digvijayassociates
