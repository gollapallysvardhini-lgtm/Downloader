Here’s a clean README for your project without emojis:

---

# Web File Downloader

A Streamlit-based web application that scans a webpage for downloadable files and allows users to download selected files in parallel with progress tracking.

## Features

* Scan any webpage for downloadable files
* Filter files by extension (`.zip`, `.iso`, `.tar.gz`, `.tgz`, etc.)
* Display file sizes before downloading
* Select multiple files for download
* Parallel downloads using multithreading
* Real-time progress bars and status updates
* Retry mechanism for failed downloads

## Supported File Types

* `.tgz`
* `.img`
* `.zip`
* `.tar.gz`
* `.gz`
* `.iso`

You can modify the `ALL_EXTENSIONS` list in the code to support additional file types.

## Installation

1. Clone the repository:

```
git clone https://github.com/your-username/web-file-downloader.git
cd web-file-downloader
```

2. Install dependencies:

```
pip install -r requirements.txt
```

If you don’t have a requirements file, install manually:

```
pip install streamlit requests beautifulsoup4
```

## Usage

Run the Streamlit app:

```
streamlit run app.py
```

Then open the local URL shown in your terminal (usually [http://localhost:8501](http://localhost:8501)).

## How It Works

1. Enter a webpage URL
2. Select desired file extensions
3. Click "Scan for Files"
4. Choose files from the results
5. Specify a download folder
6. Click "Download Selected Files"

## Project Structure

```
.
├── app.py
├── downloads/
└── README.md
```

## Notes

* The app uses HTTP requests and HTML parsing, so it works best with static pages.
* JavaScript-rendered content may not be detected.
* File size detection depends on server headers and may not always be available.
* Large files may take time depending on your network speed.

## Limitations

* No authentication support for protected pages
* No resume support for interrupted downloads
* Limited error handling for edge cases
* Relies on `HEAD` requests for file size, which some servers block

## Future Improvements

* Add support for authentication (login/session)
* Resume interrupted downloads
* Better error handling and logging
* UI improvements for large file lists
* Support for recursive crawling

## License

This project is open-source and available under the MIT License.

---

If you want, I can also:

* add a requirements.txt
* convert this into a GitHub-ready version with badges
* or simplify it for beginners
