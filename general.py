import os

# Creates a separate project folder for each website crawled
def create_project_dir(directory):
	if not os.path.exists(directory):
		print("Creating project " + directory)
		os.makedirs(directory)

# Creates queue and crawled files
def create_data_files(name, url):
	queue = os.path.join(name, "queue.txt")
	crawled = os.path.join(name, "crawled.txt")
	if not os.path.isfile(queue):
		write_file(queue, url)
	if not os.path.isfile(crawled):
		write_file(crawled, "")

# Creates new file
def write_file(path, data):
	f = open(path, "w")
	f.write(data)
	f.close()


# Add data to existing file
def append_to_file(path, data):
	with open(path, "a") as file:
		file.write(data + "\n")

# Delete contents of file:
def delete_file_contents(path):
	with open(path, "w"):
		pass


# Covert each line of file to set
def file_to_set(filename):
	res = set()
	with open(filename, "rt") as f:
		for line in f:
			res.add(line.replace("\n", ""))
	return res

# Iterate through items in set, converting each to new line in file
def set_to_file(links, file):
	delete_file_contents(file)
	for link in sorted(links):
		append_to_file(file, link)

