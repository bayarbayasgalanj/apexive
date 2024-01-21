# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Apexive Custom module',
    'version': '1.0.1',
    'category': 'HR',
    'icon': 'bayarApexive/static/description/app_icon.png',
    'sequence': 20,
    'author': 'Bayarbayasgalan, candidate of Senior Python Odoo Engineer',
    'summary': 'Attendance of Odoo',
    'description': """
Modification of Attendance Module in Odoo
Enhance the existing Attendance module in Odoo to allow users to:
Select a Project: Users should be able to choose a specific project while checking in.
Select a Project Task: Along with selecting a project, users should also be able to select a specific task related to the chosen project.
Write Descriptions: Enable users to add a description for their activities during both check-in and check-out.
    """,
    'depends': ['hr_attendance','project'],
    'data': [
        'security/bb_security.xml',
        'security/ir.model.access.csv',
        'views/inherit_hr_attendance_view.xml',
    ],
    'qweb': [],
    'images': ["static/description/images/ss1.png","static/description/images/ss2.png","static/description/images/ss3.png","static/description/images/ss4.png","static/description/images/ss5.png"],
    'website': 'https://www.linkedin.com/in/bayarbayasgalan-jagdal/',
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'assets': {
        'web.assets_backend': [
            'bayarApexive/static/src/js/inherit_my_attendance.js',
            'bayarApexive/static/src/xml/**/*',
        ],
    },
}
