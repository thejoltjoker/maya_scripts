#!/usr/bin/env python
'''
remove_maya_student_version.py
Description of remove_maya_student_version.py.
'''

import os


def main(input_file):
    '''docstring for main'''
    # dir_name, file_name = os.path.split(input_file)
    name, ext = os.path.splitext(input_file)
    suffix = 'updated'
    f = open(input_file, 'r')
    lines = f.readlines()
    f.close()

    prev_percentage = 0
    new_name = "{}_{}{}".format(name, suffix, ext)
    print new_name
    new = open(new_name, 'w')
    for i, line in enumerate(lines):
        if line != 'fileInfo "license" "student";\n':
            new.write(line)

        percentage = int(float(i) / float(len(lines)) * 100)
        cur_item = "({}/{})".format(i, len(lines))
        if percentage > prev_percentage:
            print "Complete: ", percentage, "%", cur_item, "\r",

        prev_percentage = percentage
    print "Complete: 100%", cur_item, "\r",
    # print "Student version removal done!"
    new.close()


if __name__ == '__main__':
    main('C:/Users/sequence/Downloads/armchair_covered.ma')
