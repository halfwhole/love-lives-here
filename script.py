import json
import pandas as pd

INPUT_FILE = 'raw_data.txt'
OUTPUT_CSV_FILE = 'data.csv'
OUTPUT_JSON_FILE = 'data.json'

def process(batch):
    def transform(entry):
        name = entry['n'].strip()
        message = entry['m'].strip()
        splitted = entry['d'].split('|')
        coordinates = [float(splitted[2]), float(splitted[1])]
        return {'name': name, 'message': message, 'coordinates': coordinates}

    batch = batch.strip()
    raw_data = batch.split(": ", 1)[1] # Remove `"stringValue": `
    data = json.loads(json.loads(raw_data))
    data = [transform(entry) for entry in data]

    return data


def geo_jsonize(data):
    def transform_to_feature(entry):
        return {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": entry['coordinates']
            },
            "properties": {
                "name": entry['name'],
                "message": entry['message']
            }
        }

    return {
        "type": "FeatureCollection",
        "features": [transform_to_feature(entry) for entry in data]
    }


if __name__ == '__main__':
    f = open(INPUT_FILE, 'r')
    text = f.readlines()

    ## LINES 71, 89, 106
    long_line_nums = [i for i in range(len(text)) if len(text[i]) > 1000]
    batches = [process(text[line_num]) for line_num in long_line_nums]
    data = [entry for batch in batches for entry in batch]

    ## Export to CSV
    df = pd.DataFrame(data)
    df.to_csv(OUTPUT_CSV_FILE, index=False)

    ## Export to GeoJSON
    geojson = geo_jsonize(data)
    json.dump(geojson, open(OUTPUT_JSON_FILE, 'w'))
