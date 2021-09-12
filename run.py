"""
Main program run file


"""
import json

from flask import Flask, render_template

import testBRTFRC
import testDOS
import testJSONJCTN
import testXSS
from test_resaults import TestRes

app = Flask(__name__)


@app.route('/dashboard')
@app.route('/')
def dashboard():
    data = {}

    brt1 = TestRes("bruteforce simple", testBRTFRC.simple_brtfrc(), "got into system").writeToJson()
    brt2 = TestRes("bruteforce dictionary", testBRTFRC.rand(), "passed dictionary").writeToJson()
    brt3 = TestRes("bruteforce random", testBRTFRC.dict(), "Did not block").writeToJson()

    brt_list = [brt1, brt2, brt3]
    data["Authentication Bruteforce"] = brt_list

    dos1 = TestRes("DoS simple", testDOS.testDOS(), "did not block").writeToJson()
    dos2 = TestRes("Dos spoofed ip", testDOS.testDOS(spoofIP=True), "did not block").writeToJson()
    dos3 = TestRes("DoS random queries", testDOS.testDOS(randomQueries=True), "did not block").writeToJson()
    dos4 = TestRes("DoS spoofed ip + random", testDOS.testDOS(spoofIP=True, randomQueries=True), "did not block").writeToJson()

    dos_list = [dos1, dos2, dos3, dos4]
    data["Denial Of Service"] = dos_list

    xss1 = TestRes("simple redirects", testXSS.simple_redirect(), "redirected!").writeToJson()
    xss2 = TestRes("write data", testXSS.write_data(), "changed page data").writeToJson()
    xss3 = TestRes("delete data", testXSS.delete_data(), "data was deleted from page").writeToJson()

    xss_list = [xss1, xss2, xss3]
    data["Xross Site Scripting"] = xss_list

    inj1 = TestRes("simple string", testJSONJCTN.simple_string(), "was not detected").writeToJson()
    inj2 = TestRes("get data", testJSONJCTN.insert_data(), "returned data").writeToJson()
    inj3 = TestRes("insert data", testJSONJCTN.get_pass(), "file was changed").writeToJson()

    inj_list = [inj1, inj2, inj3]
    data["JSON injection"] = inj_list

    with open('data.json', 'r') as f:
        data = json.loads(f.read())

    return render_template(
        'dashboard.html',
        data=data
    )
