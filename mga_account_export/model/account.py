# -*- coding: utf-8 -*-
##############################################################################
#
#   mga_account_export module for OpenERP
#   Copyright (C) 2015-2016 MIROUNGA (<http://www.mirounga.fr/>)
#             Christophe CHAUVET <christophe.chauvet@mirounga.fr>
#
#   This file is a part of mga_account_export
#
#   mga_account_export is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   mga_account_export is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import orm
from openerp.osv import fields
from openerp.tools.translate import _


HELP_LABEL = """Format label, use these values
- $ECRITURE
- $REFERENCE
- $DESCRIPTION
- $PARTENAIRE"""


class account_journal(orm.Model):
    _inherit = 'account.journal'

    _columns = {
        'export_code': fields.char(
            'Export code', size=6,
            help='journal code for export, leave empty to use openerp code'),
        'export_label': fields.boolean(
            'Use description',
            help='Use description or reference instead of move name'),
        'export_label_format': fields.char(
            'Label format', size=64, help=HELP_LABEL),
    }

    _defaults = {
        'export_label': False,
        'export_label_format': '$ECRITURE $PARTENAIRE',
    }


class account_account(orm.Model):
    _inherit = 'account.account'

    _columns = {
        'export_code': fields.char(
            'Export code', size=16,
            help='Account code for export, leave empty to use OpenERP code'),
    }


class account_move(orm.Model):
    _inherit = 'account.move'

    _columns = {
        'is_export': fields.boolean(
            'Is exported',
            help='If check, this move have already been exported'),
    }

    def button_cancel(self, cr, uid, ids, context=None):

        for line in self.browse(cr, uid, ids, context=context):
            if line.is_export:
                raise orm.except_orm(
                    _('Error'),
                    _('You cannot cancel an export move')
                )

        return super(account_move, self).button_cancel(
            cr, uid, ids, context=context)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
