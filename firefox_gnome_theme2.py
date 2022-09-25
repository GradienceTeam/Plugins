from pathlib import Path

from yapsy.IPlugin import IPlugin

TEMPLATE = """
/* This file was overwritten by the firefox_gnome_theme2 plugin from Gradience */

:root {{
    --gnome-browser-before-load-background:        {window_bg_color};
    --gnome-accent-bg:                             {accent_bg_color};
    --gnome-accent:                                {accent_color};
    --gnome-toolbar-background:                    {window_bg_color};
    --gnome-toolbar-color:                         {window_fg_color};
    --gnome-toolbar-icon-fill:                     {window_fg_color};
    --gnome-inactive-toolbar-color:                {window_bg_color};
    --gnome-inactive-toolbar-border-color:         {headerbar_border_color};
    --gnome-inactive-toolbar-icon-fill:            {window_fg_color};
    --gnome-menu-background:                       {dialog_bg_color};
    --gnome-headerbar-background:                  {headerbar_bg_color};
    --gnome-button-destructive-action-background:  {destructive_bg_color};
    --gnome-entry-color:                           {view_fg_color};
    --gnome-inactive-entry-color:                  {view_fg_color};
    --gnome-switch-slider-background:              {view_bg_color};
    --gnome-switch-active-slider-background:       {accent_color};
    --gnome-inactive-tabbar-tab-background:        {window_bg_color};
    --gnome-inactive-tabbar-tab-active-background: rgba(255,255,255,0.025);
    --gnome-tabbar-tab-background:                 {window_bg_color};
    --gnome-tabbar-tab-hover-background:           rgba(255,255,255,0.025);
    --gnome-tabbar-tab-active-background:          rgba(255,255,255,0.075);
    --gnome-tabbar-tab-active-hover-background:    rgba(255,255,255,0.100);
    --gnome-tabbar-tab-active-background-contrast: rgba(255,255,255,0.125);
}}
"""


class FirefoxGnomeTheme2Plugin(IPlugin):
    plugin_id = "firefox_gnome_theme2"
    title = "Firefox GNOME Theme 2"

    def give_preset_settings(self, preset_settings, custom_settings=None):
        self.variables = preset_settings["variables"]

    def validate(self):
        return False, None

    def open_settings(self):
        pass

    def apply(self, dark_theme=False):
        with (
            next(Path("~/.mozilla/firefox").expanduser().glob("*.default-release"))
            / "chrome/firefox-gnome-theme/customChrome.css"
        ).open("w") as f:
            f.write(TEMPLATE.format(**self.variables))
