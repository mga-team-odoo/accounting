# -*- coding: utf-8 -*-
##############################################################################
#
#  mga_account_export module for OpenERP,
#  Copyright (C) 2016 Mirounga (<http://www.mirounga.fr>) Christophe CHAUVET
#
#  This file is a part of mga_account_export
#
#  mga_account_export is free software: you can redistribute it and/or
#  modify it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  mga_account_export is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Account Export Wizard',
    'version': '1.0',
    'category': 'Accounting & Finance',
    'description': """Export move line per journal
Format available
- CSV
- SAGE100""",
    'author': 'MIROUNGA',
    'website': 'http://www.mirounga.fr/',
    'depends': [
        'account',
    ],
    'images': [],
    'data': [
        'view/account.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'active': False,
    'license': 'AGPL-3',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
