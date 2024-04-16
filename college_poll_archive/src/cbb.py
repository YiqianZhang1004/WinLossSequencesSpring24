import csv

input_file = "college_poll_archive/processed_data/cbb_polls_trim.csv"
output_file = "college_poll_archive/processed_data/cbb_2007_to_2021.csv"

start_row = 19666
end_row = 26367

with open(input_file, "r", newline="") as infile, open(output_file, "w", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    column_titles = next(reader)
    writer.writerow(column_titles)
    
    for i, row in enumerate(reader):
        if i > start_row and i < end_row:
            writer.writerow(row)

print("Rows removed and written to output file.")
