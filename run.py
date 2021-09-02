"""
Main program run file


"""
import json

from flask import Flask, render_template

import test_resaults

app = Flask(__name__)


@app.route('/dashboard')
@app.route('/')
def dashboard():
    '''   data = {}

    brt1 = test_resaults.TestRes("", testBRTFRC.blabla, "")
    brt2 = test_resaults.TestRes("", testBRTFRC.blabla, "")
    brt3 = test_resaults.TestRes("", testBRTFRC.blabla, "")
    brt4 = test_resaults.TestRes("", testBRTFRC.blabla, "")

    brt_list = [brt1, brt2, brt3, brt4]
    data["bruteforce"] = brt_list

    dos1 = test_resaults.TestRes("", testDOS.blabla, "")
    dos2 = test_resaults.TestRes("", testDOS.blabla, "")
    dos3 = test_resaults.TestRes("", testDOS.blabla, "")
    dos4 = test_resaults.TestRes("", testDOS.blabla, "")

    dos_list = [dos1, dos2, dos3, dos4]
    data["dos"] = dos_list

    xss1 = test_resaults.TestRes("", testXSS.blabla, "")
    xss2 = test_resaults.TestRes("", testXSS.blabla, "")
    xss3 = test_resaults.TestRes("", testXSS.blabla, "")
    xss4 = test_resaults.TestRes("", testXSS.blabla, "")

    xss_list = [xss1, xss2, xss3, xss4]
    data["xss"] = xss_list

    inj1 = test_resaults.TestRes("", testJSONJCTN.blabla, "")
    inj2 = test_resaults.TestRes("", testJSONJCTN.blabla, "")
    inj3 = test_resaults.TestRes("", testJSONJCTN.blabla, "")
    inj4 = test_resaults.TestRes("", testJSONJCTN.blabla, "")

    inj_list = [inj1, inj2, inj3, inj4]
    data["json injection"] = inj_list'''



    with open('data.json', 'r') as f:
        data = json.loads(f.read())

    return render_template(
        'dashboard.html',
        data=data
    )



