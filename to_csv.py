import tabula
import pandas as pd
import json
import os


def get_all_files(directory):

    # Get a list of all files in the directory and its subdirectories
    pdf_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".pdf"):
                yield os.path.join(root, file)


def main():

    # Set the directory to search for PDF files
    directory = "./"
    for pdf_file in get_all_files(directory):
        print(pdf_file)
        # if os.path.exists('{0}.json'.format(pdf_file)):
        #     print("skip, ", '{0}.json'.format(pdf_file))
        #     continue
        try:
            # Read the PDF file and extract its contents to a JSON file
            df = tabula.read_pdf(pdf_file, pages='1')[0]
            col_names = ["CURRENCY","SYMBOL","TT BUY","TT SELL","BILL BUY","BILL SELL","TC BUY","TC SELL","CN BUY","CN SELL","PC BUY"]
            df.columns = col_names
            df.iloc[:,2:11] = df.iloc[:,2:11].apply(pd.to_numeric, errors="coerce")
            df.drop(0, inplace=True)
            df.drop(1, inplace=True)
            df.drop(2, inplace=True)
        except:
            print(pdf_file)


        json_str = df.to_json(orient='records')
        output = json.loads(json_str)
        # Write the JSON output to a file
        with open('{0}.json'.format(pdf_file), 'w') as outfile:
            json.dump(output, outfile, indent=4)


if __name__ == "__main__":
    main()