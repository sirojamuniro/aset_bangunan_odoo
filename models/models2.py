from odoo import models, fields, api, _

class ModelZona(models.Model):
    _name = 'bangunan.zona'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Model Zona'
    _rec_name = 'zona_name'

    zona_name = fields.Char(string='Nama Bangunan', required=True, track_visibility='always')
    zona_kode = fields.Char(string='Kode Zona', required=True, copy=False, readonly=True, index=True, default=lambda self: ('New'))
    area_id = fields.Many2one('bangunan.area', string='Area', required=True)

    @api.model
    def create(self, vals):
        if vals.get('zona_kode', ('New')) == ('New'):
            vals['zona_kode'] = self.env['ir.sequence'].next_by_code('bangunan.zona.sequence') or ('New')
        return super(ModelZona, self).create(vals)

