Web File Downloader

A Streamlit-based web application that scans a webpage for downloadable files and allows users to download selected files in parallel with progress tracking.

Features
Scan any webpage for downloadable files
Filter files by extension (.zip, .iso, .tar.gz, .tgz, etc.)
Display file sizes before downloading
Select multiple files for download
Parallel downloads using multithreading
Real-time progress bars and status updates
Retry mechanism for failed downloads
Supported File Types
.tgz
.img
.zip
.tar.gz
.gz
.iso

You can modify the ALL_EXTENSIONS list in the code to support additional file types.

Installation
Clone the repository:
git clone https://github.com/your-username/web-file-downloader.git
cd web-file-downloader
Install dependencies:
pip install -r requirements.txt

If you don’t have a requirements file, install manually:

pip install streamlit requests beautifulsoup4
Usage

Run the Streamlit app:

streamlit run app.py

Then open the local URL shown in your terminal (usually http://localhost:8501
).

How It Works
Enter a webpage URL
Select desired file extensions
Click "Scan for Files"
Choose files from the results
Specify a download folder
Click "Download Selected Files"
Project Structure
.
├── app.py
├── downloads/
└── README.md
