import os
import requests
import streamlit as st
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

#page
st.set_page_config(page_title="File Downloader", layout="wide")

# Supported extensions
ALL_EXTENSIONS = [".tgz", ".img", ".zip", ".tar.gz", ".gz", ".iso"]

#functions

def is_valid_url(url):
    parsed = urlparse(url)
    return parsed.scheme and parsed.netloc

def get_download_links(url):
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
    except Exception as e:
        st.error(f"Error fetching URL: {e}")
        return []

    soup = BeautifulSoup(res.text, "html.parser")
    links = []

    for a in soup.find_all("a", href=True):
        full_url = urljoin(url, a["href"])
        links.append(full_url)

    return list(set(links))


def filter_links(links, extensions):
    return [
        link for link in links
        if any(link.lower().endswith(ext) for ext in extensions)
    ]


def get_file_size(url):
    try:
        r = requests.head(url, allow_redirects=True, timeout=5)
        size = int(r.headers.get("content-length", 0))
        return round(size / (1024 * 1024), 2)  # MB
    except:
        return None


def download_file(url, folder, progress_bar, status_text, retries=3):
    filename = os.path.basename(urlparse(url).path)
    filepath = os.path.join(folder, filename)

    for attempt in range(retries):
        try:
            with requests.get(url, stream=True, timeout=10) as r:
                r.raise_for_status()
                total = int(r.headers.get("content-length", 0))
                downloaded = 0

                with open(filepath, "wb") as f:
                    for chunk in r.iter_content(8192):
                        if chunk:
                            f.write(chunk)
                            downloaded += len(chunk)

                            if total > 0:
                                progress_bar.progress(downloaded / total)

                status_text.success(f"Downloaded: {filename}")
                return True

        except Exception as e:
            status_text.warning(f"Retry {attempt+1} failed for {filename}")
            time.sleep(2)

    status_text.error(f"Failed: {filename}")
    return False


#display downloader UI

st.title("Web File Downloader")

#URL input 
st.header("Enter URL")

url = st.text_input("Webpage URL")

if url and not is_valid_url(url):
    st.error("Invalid URL format")

#file filtering
st.header("Select File Types")

selected_types = st.multiselect(
    "Choose file extensions",
    ALL_EXTENSIONS,
    default=[]
)

#fetching files
if st.button("Scan for Files"):
    if not url:
        st.warning("Please enter a URL")
    else:
        with st.spinner("Scanning webpage..."):
            links = get_download_links(url)
            filtered = filter_links(links, selected_types)

        if filtered:
            st.session_state["files"] = filtered
            st.success(f"Found {len(filtered)} matching files")
        else:
            st.warning("No files found")

#file selection and file details
if "files" in st.session_state:
    st.header("Select Files")

    selected_files = []

    for link in st.session_state["files"]:
        col1, col2 = st.columns([4, 1])

        with col1:
            checked = st.checkbox(link)

        with col2:
            size = get_file_size(link)
            if size:
                st.write(f"{size} MB")
            else:
                st.write("Unknown")

        if checked:
            selected_files.append(link)

    #dselected folders
    st.header("Selected Folders")

    dest_folder = st.text_input("Folder path", "./downloads")

    #download
    if st.button("Download Selected Files"):
        if not selected_files:
            st.warning("No files selected")
        else:
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)

            st.header("Downloading...")

            progress_elements = []
            status_elements = []

            for file in selected_files:
                progress_elements.append(st.progress(0))
                status_elements.append(st.empty())

            # Parallel downloads
            with ThreadPoolExecutor(max_workers=4) as executor:
                futures = []

                for i, file in enumerate(selected_files):
                    futures.append(
                        executor.submit(
                            download_file,
                            file,
                            dest_folder,
                            progress_elements[i],
                            status_elements[i]
                        )
                    )

                for future in as_completed(futures):
                    pass

            st.success("All downloads completed")