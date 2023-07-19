import os, urllib.request, requests

if not os.path.exists("links.txt"):
	fl = open("links.txt", 'w')
	fl.write("# enter links on separate lines")
	fl.close()

	print("file \"links.txt\" does not exist. it has been created in \"" + os.getcwd() + "\" - open it in a text editor")
	input("enter to exit...")
	
	exit()

fl = open("links.txt", 'r')

if not os.path.exists("output/"):
	os.mkdir("output/")

lines = fl.read().splitlines()

for link in lines:
	if len(link) == 0: continue
	if link[0] == "#": continue

	print(link)
	r = requests.get(link)

	if r.status_code == requests.codes.ok:
		print("success!!")
	else:
		print("failed")

	with open("output/" + os.path.basename(link), 'wb') as file:
		file.write(r.content)

