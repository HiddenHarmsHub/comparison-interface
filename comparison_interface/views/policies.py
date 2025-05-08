import os

from ..configuration.website import Settings as WS
from .request import Request


class Policies(Request):
    """Render the policies page.

    This page either contains an iframe with a link to a google doc or the html from the location specified.
    """

    def get(self, _):
        """Request get handler."""
        if WS.configuration_has_key(WS.BEHAVIOUR_SITE_POLICIES_LINK, self._app):
            return self._render_template(
                'pages/policies.html',
                {
                    'google_doc': True,
                    'site_policies_link': WS.get_behaviour_conf(WS.BEHAVIOUR_SITE_POLICIES_LINK, self._app),
                    'site_policies_back_button': WS.get_text(WS.SITE_POLICIES_BACK_BUTTON_LABEL, self._app),
                },
            )
        # otherwise we are have html to inject instead which could either be a fragment of a full page
        site_policies_html = WS.get_behaviour_conf(WS.BEHAVIOUR_SITE_POLICIES_HTML, self._app)
        with open(os.path.join(self._app.root_path, site_policies_html)) as input_file:
            html = input_file.read()

        if html.startswith('<html'):
            fragment = False
        else:
            fragment = True
        return self._render_template(
            'pages/policies.html',
            {
                'google_doc': False,
                'fragment': fragment,
                'html_string': html,
                'site_policies_back_button': WS.get_text(WS.SITE_POLICIES_BACK_BUTTON_LABEL, self._app),
            },
        )
