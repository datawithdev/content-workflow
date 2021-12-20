#! /usr/bin/env python3
import configparser
import os
import json
from pyairtable import Table

config_file = "config.debug.ini"
config = configparser.ConfigParser()
config.read(config_file)
base_id = config['airtable']['base_id']
api_key = config['airtable']['api_key']
table_name = config['airtable']['table_name']
folder_prefix = config['airtable']['folder_prefix']



def checkKey(dict, key):
    if key in dict:
        return True
    else:
        return False

def unEscape(inputtext):
    return True

def main():
    try:
        table = Table(api_key, base_id, table_name)

        for records in table.iterate(page_size=100, max_records=1000):
            for record in records:
                category=''
                h1_title = ''
                introduction = ''
                topic_parent_slug = ''
                topic_slug = ''
                section1_h2_title = ''
                section2_h2_title = ''
                section3_h2_title = ''
                section4_h2_title = ''
                section5_h2_title = ''
                section6_h2_title = ''
                section1_details = ''
                section2_details = ''
                section3_details = ''
                section4_details = ''
                section5_details = ''
                section6_details = ''
                # y = json.loads(x)
                if checkKey( record['fields'], 'category' ):
                    category = (record['fields']['category'])
                if checkKey( record['fields'], 'h1_title' ):
                    h1_title = (record['fields']['h1_title'])
                if checkKey( record['fields'], 'introduction' ):
                    introduction = (record['fields']['introduction'])
                if checkKey( record['fields'], 'topic_parent_slug' ):
                    topic_parent_slug = (record['fields']['topic_parent_slug'])
                if checkKey( record['fields'], 'topic_slug' ):
                    topic_slug = (record['fields']['topic_slug'])
                if checkKey( record['fields'], 'section1_h2_title' ):
                    section1_h2_title = (record['fields']['section1_h2_title'])
                if checkKey( record['fields'], 'section2_h2_title' ):
                    section2_h2_title = (record['fields']['section2_h2_title'])
                if checkKey( record['fields'], 'section3_h2_title' ):
                    section3_h2_title = (record['fields']['section3_h2_title'])
                if checkKey( record['fields'], 'section4_h2_title' ):
                    section4_h2_title = (record['fields']['section4_h2_title'])
                if checkKey( record['fields'], 'section5_h2_title' ):
                    section5_h2_title = (record['fields']['section5_h2_title'])
                if checkKey( record['fields'], 'section6_h2_title' ):
                    section6_h2_title = (record['fields']['section6_h2_title'])
                if checkKey( record['fields'], 'section1_details' ):
                    section1_details = (record['fields']['section1_details'])
                if checkKey( record['fields'], 'section2_details' ):
                    section2_details = (record['fields']['section2_details'])
                if checkKey( record['fields'], 'section3_details' ):
                    section3_details = (record['fields']['section3_details'])
                if checkKey( record['fields'], 'section4_details' ):
                    section4_details = (record['fields']['section4_details'])
                if checkKey( record['fields'], 'section5_details' ):
                    section5_details = (record['fields']['section5_details'])
                if checkKey( record['fields'], 'section6_details' ):
                    section6_details = (record['fields']['section6_details'])


                if len(topic_slug) < 3 or len(category) < 3 or len(topic_parent_slug)<3 or len(introduction) < 10:
                    continue


                str = "---\ntitle: {0}\nmenu_order: 2\ntaxonomy:\n    category: {1}\n---\n\n"


                str = str.format(h1_title,category)
                # print(str)

                str =    str + introduction + '\n' + section1_h2_title + '\n' + section1_details +  '\n' + section2_h2_title + '\n' + section2_details  + '\n' + section3_h2_title + '\n' + section3_details + '\n' + section4_h2_title + '\n' + section4_details + '\n' + section5_h2_title + '\n' + section5_details

                # print('topic_parent_slug: ' + topic_parent_slug)
                # print('topic_slug: ' + topic_slug)
                # print(str)
                fname = folder_prefix +topic_parent_slug+ "-" + topic_slug + '.md'
                # print('fname:' +fname)
                f = open(fname , "w")
                f.write(str)
                f.close()

    except KeyError:
        print("Couldn't find airtable base key or api key")
        exit(1)




if __name__ == "__main__":
    main()
