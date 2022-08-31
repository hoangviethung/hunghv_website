# -*- coding: utf-8 -*-
{
    'name': 'Theme Roger',
    'summary': 'Theme Roger Version 1.0',
    'version': '1.0',
    'author': 'Roger Hoang',
    'category': 'Theme',
    'sequence': 3000,
    'maintainer': 'Roger Hoang',
    'company': 'Hygge',
    'support': 'https://hygge.com',
    'website': 'https://hygge.com',
    'license': 'LGPL-3',
    'depends': [
        # Odoo
        'website',
    ],
    'data': [
        'views/website_templates.xml',
        'views/home.xml',
    ],
    'qweb': [],
    'assets':{
        'web.assets_frontend': [
            # Library CSS
            "/theme_roger/static/src/libs/bootstrap/icons/bootstrap-icons.css",
            "/theme_roger/static/src/libs/owl-carousel/css/owl.carousel.min.css",
            "/theme_roger/static/src/libs/magnific/magnific-popup.css",
            # Website UI Kit
            "/theme_roger/static/src/scss/mixin.scss",
            "/theme_roger/static/src/scss/header.scss",
            "/theme_roger/static/src/scss/footer.scss",
            "/theme_roger/static/src/scss/button.scss",
            "/theme_roger/static/src/scss/color.scss",
            "/theme_roger/static/src/scss/grid.scss",
            "/theme_roger/static/src/scss/style.scss",
            # Library JS
            "/theme_roger/static/src/libs/appear/jquery.appear.js",
            "/theme_roger/static/src/libs/one-page/jquery.nav.js",
            "/theme_roger/static/src/libs/one-page/scrollIt.js",
            # Theme JS
            "/theme_roger/static/src/js/home.js",
        ],
        'web._assets_primary_variables': [
            "/theme_roger/static/src/scss/primary_variables.scss",
            "/theme_roger/static/src/scss/fonts.scss",
        ],
        'web._assets_secondary_variables': [
            ('prepend', 'theme_roger/static/src/scss/secondary_variables.scss'),
        ],
        'web._assets_frontend_helpers': [
            ('prepend', '/theme_roger/static/src/scss/bootstrap_overridden.scss'),
        ],
        'website.assets_wysiwyg': [
            ('include', 'web._assets_helpers'),
        ],
    },
}