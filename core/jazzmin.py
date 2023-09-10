JAZZMIN_SETTINGS = {
    "site_title": "CarRacing",
    "site_header": "CarRacing",
    "site_brand": "CarRacing",
    "welcome_sign": "CarRacing",
    "search_model": ["apps.cars"],
    "show_sidebar": True,
    "changeform_format": "horizontal_tabs",
    "copyright": "CarRacing",

    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Support", "url": "https://t.me/Sungrial", "new_window": True},
        {"model": "auth.User"},
    ],
}

JAZZMIN_UI_TWEAKS = {
    "theme": "darkly"
}
