

from odoo import models, fields, api

import logging

_logger = logging.getLogger(__name__)

class ResPartnerSubIndustry(models.Model):
    _name = 'res.partner.subindustry'
    _description = 'Subindustria'

    name = fields.Char(string='Nombre', required=True)
    industry_id = fields.Many2one('res.partner.industry', string='Industria relacionada')



class ResPartner(models.Model):
    _inherit = 'res.partner'

    subindustry_id = fields.Many2one('res.partner.subindustry', string='Subindustria')
    anmat_certification = fields.Boolean(string='Certificación ANMAT')