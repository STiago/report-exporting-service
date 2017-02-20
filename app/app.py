#!env/bin/python
from flask import Flask, request, abort, make_response, render_template, \
jsonify, url_for
from jinja2 import Environment, FileSystemLoader
from report_dao import get_report_data
import os
import pdfkit

app = Flask(__name__)
app.config.from_object('config.ProductionConfig')

css_file = os.path.dirname(os.path.abspath(__file__)) + '/static/css/style.css'

@app.route('/report/<int:report_id>/pdf', methods=['GET'])
def get_pdf_report(report_id=None):
    report_data = get_report_data(report_id)
    if report_data == None :
        return report_not_found_response()
    else:
        html_out = render_template('report-template.html', **report_data)
        pdf = pdfkit.from_string(html_out, False, css = css_file)
        response = make_response(pdf)
        response.headers.set('Content-Disposition', 'attachment', filename="report"+ str(report_id) + '.pdf')
        response.headers.set('Content-Type', 'application/pdf')
        return response

@app.route('/report/<int:report_id>/xml', methods=['GET'])
def get_xml_report(report_id=None):
    report_data = get_report_data(report_id)
    if report_data == None :
        return report_not_found_response()
    else:
        template = render_template('report-template.xml', **report_data)
        response = make_response(template)
        response.headers['Content-Type'] = 'application/xml'
        return response

def report_not_found_response():
    return make_response(jsonify({'error': 'Report not found'}), 404)

if __name__ == '__main__':
    app.run(debug=app.config.get('DEBUG'), port=8080)
