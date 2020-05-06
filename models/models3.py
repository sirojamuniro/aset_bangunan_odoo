from odoo import models, fields, api, _
class ModelBangunan(models.Model):
    _name = 'bangunan.bangunan'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Model Bangunan'
    _rec_name = 'bangunan_name'
    area_id = fields.Many2one('bangunan.area', string='Area', required=True)
    bangunan_name = fields.Char(string='Nama Bangunan', required=True, track_visibility='always')
    zona_id = fields.Many2one('bangunan.zona', string='Bangunan')
    bangunan_kode = fields.Char(string='Kode Bangunan', required=True, copy=False, readonly=True, index=True, default=lambda self: ('New'))
    jenis_bangunan= fields.Selection([
        ('kantor', 'Kantor'),
        ('sekolah', 'Sekolah'),
        ('ibadah', 'Ibadah'),
        ('sosial', 'Sosial')
    ], string='Jenis Bangunan', default="kantor")
    alamat = fields.Text(string='Alamat')
    sertifikat= fields.Selection([
        ('shm', 'Surat Hak Milik'),
        ('shgb', 'Surat Hak Guna Bangunan')
    ], string='Sertifikat', default="shm")
    nomor_sertifikat= fields.Integer(string='Nomor Sertifikat', track_visibility='always')
    Keterangan = fields.Text(string='Keterangan')

    @api.model
    def create(self, vals):
        if vals.get('bangunan_kode', ('New')) == ('New'):
            vals['bangunan_kode'] = self.env['ir.sequence'].next_by_code('bangunan.bangunan.sequence') or ('New')
        return super(ModelBangunan, self).create(vals)

    @api.onchange('area_id')
    def onchange_area_id(self):
        for res in self:
            return {'domain': {'zona_id': [('area_id', '=', res.area_id.id)]}}
