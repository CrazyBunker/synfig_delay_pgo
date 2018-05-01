#!/usr/bin/env python
# -*- coding: utf-8 -*-
##
#   Author: Vladislav Plotkin aka Jake Dog
#   e-mail: vlad@krasnodar-it-service.ru	
#   web:    https://vlad.krsanodar-it-service.ru
##
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
    help="input PGO`s file")
ap.add_argument("-o", "--output", required=True,
    help="output PGO`s file")
ap.add_argument("-d", "--delay", default=0,
    help="delay time of PGO file")
args = vars(ap.parse_args())
in_f = open(args['input'],'r')
out_file = open(args['output'],'w')
count= 1
delay = int(args['delay'])
for line in in_f.readlines():
    if count < 4:
        out_f = line
    elif count == 4 or count == 5 :
        out_f = str(int(line)+delay)+'\n'
    elif count == 8:
        out_f = u'\t' + str(int(line.replace('\t',''))+delay)+'\n'
    elif count == 11:
        out_f = u'\t\t' + str(int(line.replace('\t\t',''))+delay)+'\n'
    elif u'\t\t\t\t' in line.decode('utf-8'):
        string = line.replace('\t\t\t\t','').split(' ')
        out_f = u'\t\t\t\t' + str(int(string[0])+delay)+' '+string[1]
        out_file.write(out_f.encode('utf-8'))
        count=count+1
        continue
    elif u'\t\t\t' in line.decode('utf-8'):
        string = line.decode('utf-8').replace('\t\t\t','').split(' ')
        out_f = (u'\t\t\t' + string[0]+' '+str(int(string[1])+delay)+' '+str(int(string[2])+delay)+' '+string[3]).encode('utf-8')
    else:
        out_f = line
    print count
    out_file.write(out_f)
    count=count+1
out_file.close()
in_f.close()
