# openimages V6
Download specific subset.

## Required file
Class Names:
* wget https://storage.googleapis.com/openimages/v6/oidv6-class-descriptions.csv

Train/Test/Validation Image IDs:
* wget https://storage.googleapis.com/openimages/v6/oidv6-train-images-with-labels-with-rotation.csv
* wget https://storage.googleapis.com/openimages/2018_04/validation/validation-images-with-rotation.csv
* wget https://storage.googleapis.com/openimages/2018_04/test/test-images-with-rotation.csv

Python script that downloads images from CVDF
* wget https://raw.githubusercontent.com/openimages/dataset/master/downloader.py

## Get Image IDs
Create a text file containing all the image IDs that you're interested in downloading
```
$ python image_list.py -c <subclass-names>  -d <class-names>  -p <image-ids>

optional arguments:
  -h, --help           show this help message and exit
  -c , --classes       classes name
  -d , --description   path to descriptions file
  -p , --annotation    path to annotations file

Example:
python image_list.py -c Cattle,Sheep,Goat -d oidv6-class-descriptions.csv -p oidv6-train-images-with-labels-with-rotation.csv
python image_list.py -c Cattle,Sheep,Goat -d oidv6-class-descriptions.csv -p validation-images-with-rotation.csv
python image_list.py -c Cattle,Sheep,Goat -d oidv6-class-descriptions.csv -p test-images-with-rotation.csv
```
## Start Downloading
```
$ python downloader.py <IMAGE_LIST_FILE> --download_folder <DOWNLOAD_FOLDER> --num_processes <number>

optional arguments:
  -h, --help           show this help message and exit
  --num_processes      Number of parallel processes to use (default is 5).
  --download_folder    Folder where to download the images.
  
  Example:
  python downloader.py train.txt --download_folder /home/lab/myfolder/ --num_processes 5
  python downloader.py test.txt --download_folder /home/lab/myfolder/ --num_processes 5
  python downloader.py validation.txt --download_folder /home/lab/myfolder/ --num_processes 5
```
