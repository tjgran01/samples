import csv
import os

def list_files(data_dir):
    """Prints all of the files in the data directory out to the console window.
        Args:
            data_dir(str): The location of the directory in where data
            files are stored.
        Returns:
            fname_list(list): A list of all the file names in the data
            directory."""

    fname_list = []
    for fname in os.listdir(data_dir):
        fname_list.append(fname)

    return fname_list


def read_in_file(fname):

    with open(fname, "r") as in_csv:
        csv_obj = csv.reader(in_csv, delimiter=",")
        data = []
        for row in csv_obj:
            data.append(row)
        return data

def get_cols(csv_file):

    headings = csv_file[0]
    all_cols = []
    for idx, heading in enumerate(headings):
        col_vals = []
        for row in csv_file:
            for i, cell in enumerate(row):
                if i == idx:
                    col_vals.append(cell)
        all_cols.append(col_vals)
    return all_cols

def get_means(all_cols):

    for col in all_cols:
        variable = col.pop(0)
        col_total = 0
        for cell in col:
            cell = int(cell)
            col_total += cell
        mean = col_total / len(col)
        print(f"Mean Value - {variable}: {mean}")


def main():

    data_dir = f"{os.getcwd()}/../data/"
    fname_list = list_files(data_dir)

    for fname in fname_list:
        print(fname)
        csv_file = read_in_file(f"{data_dir}{fname}")
        all_cols = get_cols(csv_file)
        get_means(all_cols)


if __name__ == "__main__":
    main()
