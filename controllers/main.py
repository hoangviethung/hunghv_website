from odoo import http
from odoo.addons.web.controllers.main import Home
from odoo.http import request

class ThemeRogerController(Home):
    @http.route(['/'], type='http', auth="public", website=True, sitemap=True)
    def Home(self, **opt):
        return request.render("hunghv_website.home")