from yapsy.IPlugin import IPlugin


class FirefoxGnomeThemePlugin(IPlugin):
    title = "Firefox Gnome Theme"
    author = "Gradience Team"
    description = "This plugin will customize the Gnome theme for Firefox"
    colors = None
    palette = None
    plugin_id = "firefox_gnome_theme"
    # Custom settings shown on a separate view
    custom_settings = {}
    # A dict to alias parameters to different names
    # Key is the alias name, value is the parameter name
    # Parameter can be any key in colors, palette or custom settings
    alias_dict = {}

    def activate(self):
        pass

    def deactivate(self):
        pass
    
    def load_custom_settings(self, settings):
        for setting_key, setting in self.custom_settings.items():
            self.custom_settings[setting_key].set_value(settings[setting_key])

    def get_custom_settings_for_preset(self):
        setting_dict = {}
        for setting_key, setting in self.custom_settings.items():
            return setting_dict[setting_key]
        
    def open_settings(self):
        print("SETTINGS :D")
        
    def validate(self):
        if self.colors and self.palette:
            return False, None
        else:
            return True, {
                        "error": "Missing colors or palette",
                        "element": "plugin",
                        "line": self.plugin_id,
                    }
    
    def apply(self, dark_theme=False):      
        pass
    
    def save(self):
        pass
    

