"""
Main program run file


"""
import json

from flask import Flask, render_template

from test_resaults import TestRes

app = Flask(__name__)


@app.route('/dashboard')
@app.route('/')
def dashboard():
    data = {}

    brt1 = TestRes("", testBRTFRC.blabla, "").writeToJson()
    brt2 = TestRes("", testBRTFRC.blabla, "").writeToJson()
    brt3 = TestRes("", testBRTFRC.blabla, "").writeToJson()
    brt4 = TestRes("", testBRTFRC.blabla, "").writeToJson()

    brt_list = [brt1, brt2, brt3, brt4]
    data["Authentication Bruteforce"] = brt_list

    dos1 = TestRes("", testDOS.blabla, "").writeToJson()
    dos2 = TestRes("", testDOS.blabla, "").writeToJson()
    dos3 = TestRes("", testDOS.blabla, "").writeToJson()
    dos4 = TestRes("", testDOS.blabla, "").writeToJson()

    dos_list = [dos1, dos2, dos3, dos4]
    data["Denial Of Service"] = dos_list

    xss1 = TestRes("", testXSS.blabla, "").writeToJson()
    xss2 = TestRes("", testXSS.blabla, "").writeToJson()
    xss3 = TestRes("", testXSS.blabla, "").writeToJson()
    xss4 = TestRes("", testXSS.blabla, "").writeToJson()

    xss_list = [xss1, xss2, xss3, xss4]
    data["Xross Site Scripting"] = xss_list

    inj1 = TestRes("", testJSONJCTN.blabla, "").writeToJson()
    inj2 = TestRes("", testJSONJCTN.blabla, "").writeToJson()
    inj3 = TestRes("", testJSONJCTN.blabla, "").writeToJson()
    inj4 = TestRes("", testJSONJCTN.blabla, "").writeToJson()

    inj_list = [inj1, inj2, inj3, inj4]
    data["JSON injection"] = inj_list

    with open('data.json', 'r') as f:
        data = json.loads(f.read())

    return render_template(
        'dashboard.html',
        data=data
    )
