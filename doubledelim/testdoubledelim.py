import csv
import sys
import os

# Convert comma-delimited CSV files to pipe-delimited files
# Usage: Drag-and-drop CSV file over script to convert it.

inputPath = "[PUT INPUT FILE HERE]"
outputPath = "[PUT OUTPUT FILE HERE]"

# https://stackoverflow.com/a/27553098/3357935
print("Converting CSV to tab-delimited file...")
with open(inputPath) as inputFile:
	with open(outputPath, 'w', newline='') as outputFile:
		reader = csv.DictReader((line.replace('||', '|') for line in inputFile), delimiter='|')
		writer = csv.DictWriter(outputFile, reader.fieldnames, delimiter='|')
		writer.writeheader()
		writer.writerows(reader)
print("Conversion complete.")
