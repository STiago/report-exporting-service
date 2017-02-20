#!env/bin/python
import os
from app import *
import unittest

class ReportExportingServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        app.config.from_object('config.TestConfig')

    def tearDown(self):
        pass # Nothing to do in the tearDown method

    def test_get_pdf_report_when_report_id_is_valid(self):
        response = self.app.get('/report/1/pdf')
        assert response.status_code == 200
        assert response.headers.get('Content-Type') == 'application/pdf'
        assert response.headers.get('Content-Disposition') == 'attachment; filename=report1.pdf'

    def test_get_xml_report_when_report_id_is_valid(self):
            response = self.app.get('/report/1/xml')
            assert response.status_code == 200
            assert response.headers.get('Content-Type') == 'application/xml'

    def test_get_pdf_report_when_report_id_is_not_valid(self):
        response = self.app.get('/report/10000/pdf')
        assert '"error": "Report not found"' in response.data
        assert response.status_code == 404

    def test_get_xml_report_when_report_id_is_not_valid(self):
            response = self.app.get('/report/10000/xml')
            assert '"error": "Report not found"' in response.data
            assert response.status_code == 404


if __name__ == '__main__':
    unittest.main()
