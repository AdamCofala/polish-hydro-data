# 🌊 Polish Hydrology Data Fetcher

This project periodically fetches hydrological data from **IMGW (danepubliczne.imgw\.pl)** and stores it as JSON files for each monitoring station. 📊

It was created because **IMGW only shows the latest measurements and not the historical ones** (which you would need for creating water level charts, trend analysis, or hydrology research). This tool solves that by storing measurements over time.

It uses **GitHub Actions** 🤖 to run automatically, keeping the dataset always up to date without any manual work.

---

## 📂 Accessing the Data

All collected data is publicly available via **raw GitHub URLs**:

* **Stations list (with names and coordinates):**

  ```
  https://raw.githubusercontent.com/AdamCofala/polish-hydro-data/refs/heads/master/stations_list.json
  ```

* **Individual station history:**

  ```
  https://raw.githubusercontent.com/AdamCofala/polish-hydro-data/refs/heads/master/data/{station_id}.json
  ```

👉 You can open these links directly in your browser 🌐 or download them programmatically using Python `requests`, `curl`, or any HTTP client.

Example in Python:

```python
import requests
url = "https://raw.githubusercontent.com/AdamCofala/polish-hydro-data/refs/heads/master/data/151140030.json"
data = requests.get(url).json()
print(data)
```

---

## ⚙️ How it Works

* `fetcher.py` downloads the latest water level data from IMGW’s public API.
* Each station has its own file stored under `data/{station_id}.json`.
* Files keep only the last **7 days** of history (rolling window).
* A global station list with coordinates is written to `stations_list.json`.

---

## 🔄 GitHub Actions

The repository is configured with GitHub Actions (via `.github/workflows/…`) to:

* Run the `fetcher.py` script on a schedule (e.g., **two times per hour** ⏱️).
* Commit updated JSON files back to the repository automatically. ✅

This means you don’t need to run anything locally – the data is **continuously refreshed and always accessible**.

---

## 🔎 Keywords for easy search

**Polish hydrology data**, **IMGW water levels**, **river water level history Poland**, **open hydrology dataset**, **hydro monitoring Poland**, **GitHub Actions water data**

---

✨ With this project, anyone can easily fetch and visualize historical water level data across Poland without needing direct access to IMGW’s internal systems.
