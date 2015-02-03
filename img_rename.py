#!/usr/bin/python3
# Rename uploaded images to match students' usernames (matric numbers)

import pymysql
import os, sys

conn = pymysql.connect(host='localhost', port=3306, user='username', passwd='password', db='db')

cur = conn.cursor()
cpath = os.getcwd()
sep = '/'
seq = (cpath, "StudentPassport")
path = sep.join(seq) # path to old images

seq2 = (path, "new_images")
path2 = sep.join(seq2) # path to new images

cur.execute("SELECT matricno, imagename FROM students_records")

for r in cur.fetchall():

    matric = str(r[0])
    imagename = str(r[1])

    # original image name
    sep1 = '/'
    seq1 = (path, imagename)    
    original_image = sep1.join(seq1)

    # new image name from matric no field
    sep3 = '/'
    seq3 = (path2, matric)    
    new_image = sep3.join(seq3)
    new_image_ext = new_image + '.jpg'

    if os.path.isfile(original_image):
        # make copies of the original name with new names, skip rows where no image found
        os.rename(original_image, new_image_ext)
        # print("true", original_image)
    else:
        pass
cur.close()
conn.close()

