import os

from ..configuration.website import Settings as WS
from .request import Request


class Policies(Request):
    """Render the policies page.

    This page contains an iframe with a link to a google doc containing the site policies.
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
        # otherwise we are have html to inject instead
        site_policies_link = WS.get_behaviour_conf(WS.BEHAVIOUR_SITE_POLICIES_HTML, self._app)
        with open(os.path.join(self._app.root_path, site_policies_link)) as input_file:
            html_fragment = input_file.read()

        return self._render_template(
            'pages/policies.html',
            {
                'google_doc': False,
                'html_string': html_fragment,
                'site_policies_back_button': WS.get_text(WS.SITE_POLICIES_BACK_BUTTON_LABEL, self._app),
            },
        )
