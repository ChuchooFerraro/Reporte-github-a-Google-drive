from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

upload_file = ['issues.xlsx']
for file in upload_file:
	gfile = drive.CreateFile({'parents': [{'id': '1liQHDJBCCfEemFv2uPpXSv6PMtx2t00Q'}]})
	# Read file and set it as the content of this instance.
	gfile.SetContentFile(file)
	gfile.Upload() # Upload the file.