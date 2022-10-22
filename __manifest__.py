# -*- coding: utf-8 -*-
{
    'name': 'Personal Website',
    'summary': 'Personal Website',
    'version': '1.0',
    'author': 'Hoàng Việt Hùng',
    'category': 'Website',
    'maintainer': 'Hoàng Việt Hùng',
    'company': 'Cready',
    'support': 'https://hunghv.com',
    'website': 'https://hunghv.com',
    'license': 'LGPL-3',
    'depends': [
        # Odoo
        'website',
    ],
    'installable': True,
    'data': [
        'views/website_templates.xml',
        'views/home.xml',
    ],
    'qweb': [],
    'assets':{
        'web.assets_frontend': [
            # Library CSS
            "/hunghv_website/static/src/libs/bootstrap/icons/bootstrap-icons.css",
            "/hunghv_website/static/src/libs/owl-carousel/css/owl.carousel.min.css",
            "/hunghv_website/static/src/libs/magnific/magnific-popup.css",
            # Website UI Kit
            "/hunghv_website/static/src/scss/mixin.scss",
            "/hunghv_website/static/src/scss/header.scss",
            "/hunghv_website/static/src/scss/footer.scss",
            "/hunghv_website/static/src/scss/button.scss",
            "/hunghv_website/static/src/scss/color.scss",
            "/hunghv_website/static/src/scss/grid.scss",
            "/hunghv_website/static/src/scss/website.ui.scss",
            # Library JS
            "/hunghv_website/static/src/libs/appear/jquery.appear.js",
            # Theme JS
            "/hunghv_website/static/src/js/home.js",
        ],
        'web._assets_primary_variables': [
            "/hunghv_website/static/src/scss/primary_variables.scss",
            "/hunghv_website/static/src/scss/fonts.scss",
        ],
        'web._assets_secondary_variables': [
            ('prepend', 'hunghv_website/static/src/scss/secondary_variables.scss'),
        ],
        'web._assets_frontend_helpers': [
            ('prepend', '/hunghv_website/static/src/scss/bootstrap_overridden.scss'),
        ],
        'website.assets_wysiwyg': [
            ('include', 'web._assets_helpers'),
        ],
    },
    'application': True,
}