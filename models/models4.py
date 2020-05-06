from odoo import models, fields, api, _
class ModelLantai(models.Model):
    _name = 'bangunan.lantai'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Model Lantai'
    _rec_name = 'lantai_name'
    bangunan_id = fields.Many2one('bangunan.bangunan', string='Bangunan')
    lantai_name = fields.Char(string='Nama Lantai', required=True, track_visibility='always')
    lantai_kode = fields.Char(string='Kode Lantai', required=True, copy=False, readonly=True, index=True, default=lambda self: ('New'))

    @api.model
    def create(self, vals):
        if vals.get('lantai_kode', ('New')) == ('New'):
            vals['lantai_kode'] = self.env['ir.sequence'].next_by_code('bangunan.lantai.sequence') or ('New')
        return super(ModelLantai, self).create(vals)
