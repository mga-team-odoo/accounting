# -*- coding: utf-8 -*-
##############################################################################
#
#  account_partner_generator module for OpenERP,
#  Copyright (C) 2016 Mirounga (<http://www.mirounga.fr>) Christophe CHAUVET
#
#  This file is a part of account_partner_generator
#
#  account_partner_generator is free software: you can redistribute it and/or
#  modify it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  account_partner_generator is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Account partner generator',
    'version': '1.0',
    'category': 'Accounting & Finance',
    'description': """Create easily an partner account""",
    'author': 'MIROUNGA',
    'website': 'http://www.mirounga.fr/',
    'depends': [
        'account',
    ],
    'images': [],
    'data': [
        # 'security/groups.xml',
        # 'security/ir.model.access.csv',
        'data/sequence.xml',
        'view/company.xml',
        'view/partner.xml',
        # 'report/report.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'active': False,
    'license': 'AGPL-3',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
