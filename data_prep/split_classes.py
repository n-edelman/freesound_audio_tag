import os
import csv
import shutil


with open('../data/train.csv','rb') as csvfile:
    reader = csv.reader(csvfile)
    reader.next()
    for row in reader: 
	sound = row[1]
	verified = int(row[2])
	class_dir = os.path.join('data','train_dirs',sound)

	if not os.path.isdir(class_dir):
	    os.mkdir(class_dir)

	new_fname = os.path.join(class_dir,row[0].split(".")[0]+'_'+str(verified)+'.wav')
	old_fname = os.path.join('data','audio_train',row[0])
 	shutil.move(old_fname, new_fname)




	
