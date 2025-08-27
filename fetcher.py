import requests, json, os, datetime, pathlib

API_URL = "https://danepubliczne.imgw.pl/api/data/hydro"
DATA_DIR = pathlib.Path("data")
DATA_DIR.mkdir(exist_ok=True)

def main():
    r = requests.get(API_URL)
    r.raise_for_status()
    all_data = r.json()
    now = datetime.datetime.utcnow().isoformat()

    for row in all_data:
        station_id = row["id_stacji"]
        path = DATA_DIR / f"{station_id}.json"

        # load old data if exists
        if path.exists():
            with open(path, "r", encoding="utf-8") as f:
                station_data = json.load(f)
        else:
            station_data = []

        # append new measurement
        station_data.append({
            "timestamp": now,
            "data": row
        })

        # keep file small: last 30 days only
        station_data = [
            entry for entry in station_data
            if (datetime.datetime.fromisoformat(entry["timestamp"]) >
                datetime.datetime.utcnow() - datetime.timedelta(days=7))
        ]

        # save
        with open(path, "w", encoding="utf-8") as f:
            json.dump(station_data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
