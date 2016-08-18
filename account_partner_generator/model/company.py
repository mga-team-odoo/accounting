# -*- coding: utf-8 -*-
##############################################################################
#
# account_partner_generator module for OpenERP, Generate partner account
# Copyright (C) 2016 MIROUNGA (<http://www.mirounga.fr/>)
#           Christophe CHAUVET <christophe.chauvet@gmail.com>
#
# This file is a part of account_partner_generator
#
# account_partner_generator is free software: you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the License,
# or (at your option) any later version.
#
# account_partner_generator is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import orm
from openerp.osv import fields


class res_company(orm.Model):
    _inherit = 'res.company'

    _columns = {
        'acc_aux_customer_id': fields.many2one(
            'account.account', 'Aux Customer Account',
            help='Select parent account when create a new customer account'),
        'acc_aux_supplier_id': fields.many2one(
            'account.account', 'Aux Supplier Account',
            help='Select parent account when create a new supplier account'),
        'seq_acc_customer_id': fields.many2one(
            'ir.sequence', 'Customer sequence',
            help='Select sequence to generate the suffix account code'),
        'seq_acc_supplier_id': fields.many2one(
            'ir.sequence', 'Supplier sequence',
            help='Select sequence to generate the suffix account code'),
    }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
