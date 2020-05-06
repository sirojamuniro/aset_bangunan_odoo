from odoo import models, fields, api, _



class ModelArea(models.Model):
    _name = 'bangunan.area'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Model Area'
    _rec_name = 'area_name'

    area_name = fields.Char(string='Nama Area', required=True, track_visibility='always')
    area_kode = fields.Char(string='Kode Area', required=True, copy=False, readonly=True, index=True, default=lambda self: ('New'))



    @api.model
    def create(self, vals):
        if vals.get('area_kode', ('New')) == ('New'):
            vals['area_kode'] = self.env['ir.sequence'].next_by_code('bangunan.area.sequence') or ('New')
        return super(ModelArea, self).create(vals)






