from odoo import models, fields, api, _
class ModelRuang(models.Model):
    _name = 'bangunan.ruang'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Model Ruang'
    _rec_name = 'ruang_name'
    lantai_id = fields.Many2one('bangunan.lantai', string='Lantai ID')
    ruang_name = fields.Char(string='Nama Ruang', required=True, track_visibility='always')
    ruang_kode = fields.Char(string='Kode Ruang', required=True, copy=False, readonly=True, index=True, default=lambda self: ('New'))
    bangunan_id = fields.Many2one('bangunan.bangunan', string='Ruang ID')

    @api.model
    def create(self, vals):
        if vals.get('ruang_kode', ('New')) == ('New'):
            vals['ruang_kode'] = self.env['ir.sequence'].next_by_code('bangunan.ruang.sequence') or ('New')
        return super(ModelRuang, self).create(vals)
