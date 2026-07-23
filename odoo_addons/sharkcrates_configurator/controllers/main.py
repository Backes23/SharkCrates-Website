import json

from odoo import http
from odoo.http import request


class CrateConfiguratorController(http.Controller):

    @http.route('/configurator', type='http', auth='public', website=True, sitemap=True)
    def configurator_page(self, **kwargs):
        return request.render('sharkcrates_configurator.configurator_page')

    @http.route('/configurator/submitted', type='http', auth='public', website=True,
                csrf=False, methods=['POST'])
    def configurator_submitted(self, **kwargs):
        """Called by our frontend JS once the DriveWorks embed shows its
        completion message (see static/src/js/configurator.js).

        DriveWorks' own completion event/payload isn't confirmed against
        their documented API yet, so this only receives what our JS can see
        from the DOM (the message text, page URL, timestamp). Once the real
        DriveWorks Live Integration Client API/payload is known, extend this
        to create a sale.order/crm.lead with the actual crate configuration
        instead of just logging the raw payload below.
        """
        payload = request.httprequest.get_data(as_text=True)
        request.env['website.configurator.submission'].sudo().create({
            'raw_payload': payload,
        })
        return json.dumps({'ok': True})
