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
# from openerp.osv import fields
from openerp.tools.translate import _
import logging

logger = logging.getLogger('openerp.addons.account_partner_generator')


class res_partner(orm.Model):
    _inherit = 'res.partner'

    _columns = {}

    def _decode_sequence(self, cr, uid, code, ref, context=None):
        """
        search the @ and # to cut the number for padding
        """
        if not ref:
            raise orm.except_orm(
                _('Error'),
                _('No reference defined on partner'))

        vals = code[code.find('@') + 1: code.find('#')]
        if vals.find(':') > 0:
            s, e = vals.split(':')
            s, e = int(s), int(e)
        else:
            s, e = 0, int(vals)

        return code[:code.find('@')] + ref[s:e]

    def create_customer_account(self, cr, uid, ids, context=None,
                                company_id=None):
        """
        Create the customer account if not exists
        """
        company_obj = self.pool['res.company']
        seq_obj = self.pool['ir.sequence']
        account_obj = self.pool['account.account']
        account_type_obj = self.pool['account.account.type']

        if company_id is None:
            company_id = self.pool['res.users'].browse(
                cr, uid, uid, context=context).company_id.id

        company = company_obj.browse(cr, uid, company_id, context=context)
        if not company.acc_aux_customer_id:
            raise orm.except_orm(
                _('Error'),
                _('Not parent account defined on the company %s') % company.name)

        if not company.seq_acc_customer_id:
            raise orm.except_orm(
                _('Error'),
                _('No customer sequence defined on the company %s') % company.name)

        acctype_ids = account_type_obj.search(
            cr, uid, [('code', '=', 'receivable')], context=context)

        for cust in self.browse(cr, uid, ids, context=context):
            if cust.property_account_receivable and \
               cust.property_account_receivable.type == 'receivable':
                # A receivable account is already link tho the customer account
                continue

            # We compose the code with prefix and sequence
            customer_account = seq_obj.next_by_code(
                cr, uid, 'account.account.customer', context=context)
            if '@' in customer_account:
                if '#' not in customer_account:
                    raise orm.except_orm(
                        _('Error'),
                _('Missing # on customer sequence defined on %s') % company.name)
                customer_account = self._decode_sequence(
                    cr, uid, customer_account, cust.ref)

            logger.info('Customer code %s' % (customer_account,))
            acc_ids = account_obj.search(
                cr, uid, [('company_id', '=', company_id),
                          ('code', '=', customer_account)], context=context)
            if acc_ids:
                self.write(cr, uid, [cust.id],
                           {'property_account_receivable': acc_ids[0]},
                           context=context)
                continue

            acc_data = {
                'code': customer_account,
                'name': cust.name,
                'parent_id': company.acc_aux_customer_id.id,
                'type': 'receivable',
                'user_type': acctype_ids[0],
                'active': True,
                'company_id': company_id,
                'reconcile': True,
            }
            acc_id = account_obj.create(cr, uid, acc_data, context=context)

            self.write(cr, uid, [cust.id],
                       {'property_account_receivable': acc_id}, context=context)

        return True

    def create_supplier_account(self, cr, uid, ids, context=None,
                                company_id=None):
        """
        Create the customer account if not exists
        """
        company_obj = self.pool['res.company']
        seq_obj = self.pool['ir.sequence']
        account_obj = self.pool['account.account']
        account_type_obj = self.pool['account.account.type']

        if company_id is None:
            company_id = self.pool['res.users'].browse(
                cr, uid, uid, context=context).company_id.id

        company = company_obj.browse(cr, uid, company_id, context=context)
        if not company.acc_aux_supplier_id:
            raise orm.except_orm(
                _('Error'),
                _('Not parent account defined on %s') % company.name)

        if not company.seq_acc_supplier_id:
            raise orm.except_orm(
                _('Error'),
                _('No supplier sequence defined on %s') % company.name)

        acctype_ids = account_type_obj.search(
            cr, uid, [('code', '=', 'payable')], context=context)

        for supp in self.browse(cr, uid, ids, context=context):
            if supp.property_account_payable and \
               supp.property_account_payable.type == 'payable':
                # A receivable account is already link tho the supplier account
                continue

            # We compose the code with prefix and sequence
            supplier_account = seq_obj.next_by_code(
                cr, uid, 'account.account.supplier', context=context)
            if '@' in supplier_account:
                if '#' not in supplier_account:
                    raise orm.except_orm(
                        _('Error'),
                _('Missing # on supplier sequence defined on %s') % company.name)
                supplier_account = self._decode_sequence(
                    cr, uid, supplier_account, supp.ref)

            logger.info('Supplier code %s' % (supplier_account,))
            acc_ids = account_obj.search(
                cr, uid, [('company_id', '=', company_id),
                          ('code', '=', supplier_account)], context=context)
            if acc_ids:
                self.write(cr, uid, [supp.id],
                           {'property_account_payable': acc_ids[0]},
                           context=context)
                continue

            acc_data = {
                'code': supplier_account,
                'name': supp.name,
                'parent_id': company.acc_aux_supplier_id.id,
                'type': 'payable',
                'user_type': acctype_ids[0],
                'active': True,
                'company_id': company_id,
                'reconcile': True,
            }
            acc_id = account_obj.create(cr, uid, acc_data, context=context)

            self.write(cr, uid, [supp.id],
                       {'property_account_payable': acc_id}, context=context)

        return True

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
