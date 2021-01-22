#!/usr/bin/env python3

import re
import json
import os



def txt2yaml_and_json(filename="EriksenLS-Legend.txt", directory_name="txt/2020_worlds_day1/"):

  headings = ['STARTING',
              'CHARACTERS',
              'EFFECTS',
              'INTERRUPTS',
              'LOCATIONS',
              'STARSHIPS',
              'WEAPONS',
              'DEVICES',
              'VEHICLES']

  fh = open(directory_name + filename, 'r')
  out = {}
  deck_info = re.findall(r'(.*)(LS|DS)-(.*)\.txt', filename)
  i = 0
  for lin in re.split(r'[\r\n]+', fh.read()):
    if lin != "":
      i = i + 1
      if i == 1:
        print("---")
        print('"' + lin + "\":")
        deckname = lin
        out[deckname] = {}
        user_info = re.findall(r'(.*) - (.*) - (LS|DS) (.*)', lin)
        print("  FILENAME: " + filename)
        print("  FILENAME_WITH_PATH: " + directory_name + filename)
        print("  USERINFO:")
        print("    - fullname: " + user_info[0][0])
        print("    - event: "    + user_info[0][1])
        print("    - deckside: " + user_info[0][2])
        print("    - deckname: " + user_info[0][3])
        out[deckname]['userinfo'] = {}
        out[deckname]['userinfo']['fullname'] = user_info[0][0]
        out[deckname]['userinfo']['event']    = user_info[0][1]
        out[deckname]['userinfo']['deckside'] = user_info[0][2]
        out[deckname]['userinfo']['deckname'] = user_info[0][3]
        print("  DECKINFO:")
        print("    - username: " + deck_info[0][0])
        print("    - deckside: " + deck_info[0][1])
        print("    - deckname: " + deck_info[0][2])
        out[deckname]['deckinfo'] = {}
        out[deckname]['deckinfo']['username'] = deck_info[0][0]
        out[deckname]['deckinfo']['deckside'] = deck_info[0][1]
        out[deckname]['deckinfo']['deckname'] = deck_info[0][2]
      elif lin in headings:
        print("  " + lin + ":")
        heading  = lin
        out[deckname][heading] = []
      elif (lin.isalpha() and lin.isupper()):
        print("\n\n⚠️⚠️⚠️⚠️ unknown heading: ["+lin+"] ⚠️⚠️⚠️⚠️\n\n")
        exit(1)
      else:
        card = lin
        card = re.sub(r'^[0-9]x ', '', card)
        card_info = re.findall(r'^([0-9])x (.*)', lin)
        if (len(card_info) > 0):
          card_i = 0
          while (card_i < int(card_info[0][0])):
            print("    - \"" + card + "\"")
            card_i = card_i + 1
            out[deckname][heading].append(card)
        else:
          print("    - \"" + card + "\"")
          out[deckname][heading].append(card)

  filename_json = filename.replace(".txt", ".json")
  directory_name_json = directory_name.replace("txt", "json")
  if (not (os.path.isdir(directory_name_json))):
    os.makedirs(directory_name_json)
  fo = open(directory_name_json + filename_json, "w")
  fo.write(json.dumps(out))
  fo.close()






event_directories = os.scandir('./txt/')
for event_directory in event_directories:
  if event_directory.is_dir():
    directory_name = './txt/' + event_directory.name + '/'
    event_files = os.scandir(directory_name)
    for event_file in event_files:
      if event_file.is_file():
        filename = event_file.name
        txt2yaml_and_json(filename, directory_name)





