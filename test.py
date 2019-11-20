#!/bin/python3

import math
import os
import random
import re
import sys
import json
from configparser import ConfigParser

if __name__ == '__main__':
    parser = ConfigParser()
    parser.read('C:\\Users\\asinha\\PycharmProjects\\TestProject\\Resources\\test.properties')
    apiList = []
    for section_name in parser.sections():
        print('Section:', section_name)
        print('  Options:', parser.options(section_name))
        for key, value in parser.items(section_name):
            link="C:/RMS_Reg_Auto/"+value.replace('"', '')
            module=key[:3]
            try:
                input_file = open(link)
                json_array = json.load(input_file)
            except:
                pass
            for item in json_array:
                try:
                    apiUrl = json_array[item][0]['input']['requestURL']
                except:
                    pass
                try:
                    hostName = json_array[item][0]['input']['requestHost']
                except:
                    hostName = "notFound"
                if hostName == "DTAGENT":
                    apiUrl = "https://dt-api.master.ri.rms-internal.com/v1/" + apiUrl
                elif hostName == "GEOVERSE":
                    apiUrl = "https://geoverse-metadata-api.map-dev.rms.com/" + apiUrl
                elif hostName == "PROXY":
                    apiUrl = "https://rms-proxy.master.ri.rms-internal.com/" + apiUrl
                elif hostName == "QUERYSERVICE":
                    apiUrl = "http://datastore-query-service.master.ri.rms-internal.com/" + apiUrl
                elif hostName == "EXPOSURE":
                    apiUrl = "http://exposure-api.master.ri.rms-internal.com/" + apiUrl
                elif hostName == "ARTEMIS":
                    apiUrl = "http://artemis.rms.com:3000/env/aws_master/" + apiUrl
                elif hostName == "KUDU":
                    apiUrl = "http://10.36.148.84:8051/" + apiUrl
                elif hostName == "notFound":
                    apiUrl = "https://one.master.ri.rms-internal.com/" + apiUrl
                if module=="reg":
                    suit="Weekly"
                elif module=="fr_":
                    suit="Full Regression"
                elif module=="rc_":
                    suit="Release Candidate"
                else:
                    suit="API/BVT"
                apiList.append(apiUrl+","+suit)
        finalApiList = list(dict.fromkeys(apiList))
        print(finalApiList)
        with open('apiList.csv', 'w') as f:
            for item in finalApiList:
                f.write("%s\n" % item)






