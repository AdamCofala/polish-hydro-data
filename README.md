# Hydro Data Fetcher

This project periodically fetches hydrological data from **IMGW (danepubliczne.imgw.pl)** and stores it as JSON files for each monitoring station. It uses **GitHub Actions** to run automatically, keeping the dataset up to date.

## How it works
- `fetcher.py` downloads the latest water level data from IMGW’s public API.  
- Each station has its own file stored under `data/{station_id}.json`.  
- Files keep only the last **7 days** of history.  
- A global station list with coordinates is written to `stations_list.json`.

## GitHub Actions
The repository is configured with GitHub Actions (via `.github/workflows/…`) to:
- Run the `fetcher.py` script on a schedule (e.g., two per hour).
- Commit updated JSON files back to the repository.

This means you don’t need to run anything locally – data is automatically refreshed.

## Accessing the data
All collected data is available via the raw file URLs on GitHub:

- **Stations list (with names and coordinates):**  
  ```
  https://raw.githubusercontent.com/AdamCofala/polish-hydro-data/refs/heads/master/station_list.json
  ```

- **Individual station history**  
  ```
  https://raw.githubusercontent.com/AdamCofala/polish-hydro-data/refs/heads/master/data/{station_id}.json
  ```

👉 Tip: you can open these links directly in your browser or download them programmatically using `requests`, `curl`, or any HTTP client.

## Running locally
If you want to run the fetcher manually on your machine:

```bash
git clone https://github.com/<username>/<repository>.git
cd <repository>
pip install -r requirements.txt  # (requires requests)
python fetcher.py
```

The script will:
- Create/update files under `data/`.
- Refresh `stations_list.json`.
