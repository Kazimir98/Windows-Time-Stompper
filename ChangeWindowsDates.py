import subprocess

def change_created_stamp(file, month, day, year, hour, minute):
	subprocess.call([
		"C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe", 
		";", 
		"$(Get-Item %s).creationtime=$(Get-Date \"%d/%d/%d %d:%d\")" 
		% (file, month, day, year, hour, minute)])
		
def change_write_stamp(file, month, day, year, hour, minute):
	subprocess.call([
		"C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe", 
		";", 
		"$(Get-Item %s).lastwritetime=$(Get-Date \"%d/%d/%d %d:%d\")" 
		% (file, month, day, year, hour, minute)])

def change_access_stamp(file, month, day, year, hour, minute):
	subprocess.call([
		"C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe", 
		";", 
		"$(Get-Item %s).lastaccesstime=$(Get-Date \"%d/%d/%d %d:%d\")" 
		% (file, month, day, year, hour, minute)])

print "Enter the file (ex. C:\\Users\\Kaz\\Documents\\stompit.doc):"
file = raw_input(">")
print "Enter the day to change it to: "
day = raw_input(">")
day = int(day)
print "Enter the month to change it to (as a number): "
month = raw_input(">")
month = int(month)
print "Enter the year to change it to: "
year = raw_input(">")
year = int(year)
print "Enter the hour to change it to (24 hour): "
hour = raw_input(">")
hour = int(hour)
print "Enter the minute to change it to: "
minute = raw_input(">")
minute = int(minute)
print "What should be stompped? 0=created, 1=modified, 2=accessed, 3=all"
choice = raw_input(">")
choice = int(choice)
if choice == 0:
	change_created_stamp(file, month, day, year, hour, minute)
elif choice == 1:
	change_write_stamp(file, month, day, year, hour, minute)
elif choice == 2:
	change_access_stamp(file, month, day, year, hour, minute)
elif choice == 3:
	change_created_stamp(file, month, day, year, hour, minute)
	change_write_stamp(file, month, day, year, hour, minute)
	change_access_stamp(file, month, day, year, hour, minute)
else:
	print "Not a valid option."