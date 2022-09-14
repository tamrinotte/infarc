# INFINITY ARCHIVE
![InfinityArchiveLogo](https://cdn.pixabay.com/photo/2016/10/25/18/18/book-1769625_960_720.png)

Infinity Archive is a command line tool to archive files and folder by compressing them.

## INSTALLATION
1) ```git clone https://github.com/tamrinotte/arcj.git```
2) ```cd infarc```
3) ```sudo cp infarc /usr/bin```
4) ```sudo chown $USER:$USER /usr/bin/infarc && sudo chmod u+x /usr/bin/infarc```

## OPTIONS 
	-c, --compress
		Use this option to compress files
	-e, --extract
		Use this option to extract files from a compressed folder
	-t, --tar
		Use this option to set the comppress type to tar
	-z, --zip
		Use this option to set the comppress type to zip
	-n, --no-hidden
		Ignore all the hidden folders
		
## EXAMPLES
	infarc -c -t <source path> <destionation path>
	infarc -c -z <source path> <destionation path>
	infarc -c -z -n <source path> <destionation path>
	infarc -c -t -n <source path> <destionation path>
	infarc -e <source path> <destionation path>
