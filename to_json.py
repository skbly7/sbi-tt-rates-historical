import tabula
import pandas as pd
import json
import os

def pdf_to_json(filepath):
    json_str = {}
    try:
        # Read the PDF file and extract its contents to a JSON file
        df = tabula.read_pdf(filepath, pages='1')[0]
        col_names = ["CURRENCY","SYMBOL","TT BUY","TT SELL",\
            "BILL BUY","BILL SELL","TC BUY","TC SELL",
            "CN BUY","CN SELL","PC BUY"]
        df.columns = col_names
        df.iloc[:,2:11] = df.iloc[:,2:11].apply(pd.to_numeric, errors="coerce")
        # drop first 3 rows
        df.drop(0, inplace=True)
        df.drop(1, inplace=True)
        df.drop(2, inplace=True)
        json_str = df.to_json(orient='records')
    except:
        print(filepath)

    return json_str

def reformat(original_records):
    new_records = {}
    for record in original_records:
        symbol = record['SYMBOL']
        values = {k: v for k, v in record.items() if k != 'SYMBOL'}
        new_records[symbol] = values
    return new_records

if __name__ == "__main__":
    filepath = os.path.join('2022', '01', '2022-01-01-14:15.pdf') # 2022/01/2022-01-01-14:15.pdf
    data = pdf_to_json(filepath)
    # #TODO transform using dataframe
    reformatted_data = reformat(json.loads(data))
    json_filepath = filepath.replace(".pdf", ".json")
    with open(json_filepath, 'w') as f:
        json.dump(reformatted_data, f, indent=4)
