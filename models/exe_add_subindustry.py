

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
    
    industry_id = fields.Many2one('res.partner.industry', string='Industria')
    subindustry_id = fields.Many2one(
        'res.partner.subindustry',
        string='Subindustria',
        domain="[('industry_id', '=', industry_id)]"
    )

    #campo existente
    #subindustry_id = fields.Many2one('res.partner.subindustry', string='Subindustria')
    anmat_certification = fields.Boolean(string='Certificación ANMAT')
    subclient_id = fields.Many2one('res.partner.subclient', string='Subcliente')
    cufe_expiration_attachment = fields.Binary(string='Vencimiento CUFE')
    cufe_expiration_filename = fields.Char(string='Nombre del archivo CUFE')

class ResPartnerSubIClient(models.Model):
    _name = 'res.partner.subclient'
    _description = 'Subcliente'

    name = fields.Char(string='Nombre', required=True)
    client_id = fields.Many2one('res.partner', string='Cliente relacionado')