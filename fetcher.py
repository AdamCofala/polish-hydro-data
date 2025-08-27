import requests, json, datetime, pathlib

API_URL = "https://danepubliczne.imgw.pl/api/data/hydro"
DATA_DIR = pathlib.Path("data")
DATA_DIR.mkdir(exist_ok=True)


def parse_ts(ts: str) -> datetime.datetime:
    """Parse ISO timestamp and ensure it's UTC-aware."""
    dt = datetime.datetime.fromisoformat(ts)
    if dt.tzinfo is None:
        return dt.replace(tzinfo=datetime.UTC)
    return dt


def main():
    r = requests.get(API_URL)
    r.raise_for_status()
    all_data = r.json()
    now = datetime.datetime.now(datetime.UTC).isoformat()

    dict_file_path = DATA_DIR / "stations.json"

    info_data = []

    for row in all_data:
        station_id = row["id_stacji"]
        path = DATA_DIR / f"{station_id}.json"

        # load old data if exists
        if path.exists():
            with open(path, "r", encoding="utf-8") as f:
                station_data = json.load(f)
        else:
            station_data = []

        add_entry = True
        if station_data:
            last_entry = station_data[-1]["data"]
            if last_entry["stan_wody_data_pomiaru"] == row["stan_wody_data_pomiaru"]:
                add_entry = False

        if add_entry:
            station_data.append({
                "timestamp": now,
                "data": row
            })

        cutoff = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=7)
        station_data = [
            entry for entry in station_data
            if parse_ts(entry["timestamp"]) > cutoff
        ]

        with open(path, "w", encoding="utf-8") as f:
            json.dump(station_data, f, ensure_ascii=False, indent=2)

        info_data.append({"id": row['id_stacji'], "station": row['stacja'], "lon": row['lon'], "lat": row['lat']})
        with open(dict_file_path, "w", encoding="utf-8") as f:
            json.dump(info_data, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
