import os

from ..configuration.website import Settings as WS
from .request import Request


class Introduction(Request):
    """Render the introduction page.

    This page either contains an iframe with a link to a google doc or the html from the location specified.
    """

    def get(self, _):
        """Request get handler."""
        if WS.configuration_has_key(WS.BEHAVIOUR_USER_INSTRUCTION_LINK, self._app):
            return self._render_template(
                'pages/introduction.html',
                {
                    'google_doc': True,
                    'user_instruction_link': WS.get_behaviour_conf(WS.BEHAVIOUR_USER_INSTRUCTION_LINK, self._app),
                    'introduction_continue_button': WS.get_text(WS.INTRODUCTION_CONTINUE_BUTTON_LABEL, self._app),
                },
            )
        # otherwise we are have html to inject instead
        user_instruction_html = WS.get_behaviour_conf(WS.BEHAVIOUR_USER_INSTRUCTION_HTML, self._app)
        with open(os.path.join(self._app.root_path, user_instruction_html)) as input_file:
            html = input_file.read()

        if html.startswith('<html'):
            fragment = False
        else:
            fragment = True
        return self._render_template(
            'pages/introduction.html',
            {
                'google_doc': False,
                'fragment': fragment,
                'html_string': html,
                'introduction_continue_button': WS.get_text(WS.INTRODUCTION_CONTINUE_BUTTON_LABEL, self._app),
            },
        )
