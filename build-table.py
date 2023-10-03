import csv
import tabulate


with open("DEEDS.csv") as f:
	data = list(csv.DictReader(f))

data = [
	row
	for row in data
	if row["Exported"] == "TRUE"
]
print(data)


table = [
	["Shelfmark", "Holding Institution", "Century", "Script", "Content", "Description"]
]
for row in data:
	table.append(
		[
			f"[{row['Shelfmark']}](./data/{row['Folder']})",
			f"[{row['Holding Institution']}]({row['Online Link']})",
			row["Script Type"],
			row["Range (e.g. 1v-5r)"],
			row["Content (Details about the content, title, etc)"]

		]
	)
print(
	tabulate.tabulate(table, headers="firstrow", tablefmt="github")
	)