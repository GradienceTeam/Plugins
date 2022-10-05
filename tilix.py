from pathlib import Path

from yapsy.IPlugin import IPlugin

TEMPLATE = """
{{
    "name": "Gradience for Tilix",
    "comment": "Gradience auto generated theme for Tilix",
    "use-theme-colors": false,
    "foreground-color": "{window_fg_color}",
    "background-color": "{window_bg_color}",
    "palette": [
        "",
        "#cc241d",
        "#98971a",
        "#d79921",
        "#458588",
        "#b16286",
        "#689d6a",
        "#a89984",
        "#928374",
        "#fb4934",
        "#b8bb26",
        "#fabd2f",
        "#83a598",
        "#d3869b",
        "#8ec07c",
        "#ebdbb2"
    ]
}}
"""



class TilixPlugin(IPlugin):
    plugin_id = "tilix"
    title = "Tilix"
    author = "Gradience Team"
    template = TEMPLATE

    def give_preset_settings(self, preset_settings, custom_settings=None):
        self.variables = preset_settings["variables"]
        self.palettes = preset_settings["palettes"]

    def validate(self):
        return False, None

    def open_settings(self):
        return False

    def apply(self, dark_theme=False):
        for path in ["~/.config/tilix/schemes/"]:
            try:
                with (
                    next(Path("~/.config/tilix/schemes/gradience.json").expanduser().glob("*.*"))
                ).open("w") as f:
                    f.write(self.template.format(**self.variables, **self.palettes))
            except OSError:
                pass
            except StopIteration:
                pass
