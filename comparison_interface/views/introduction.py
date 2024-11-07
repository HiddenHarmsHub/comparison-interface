from ..configuration.website import Settings as WS
from .request import Request


class Introduction(Request):
    """Render the introduction page.

    This page contains an iframe with a link to a google doc with text introducing the project.
    """

    def get(self, _):
        """Request get handler."""
        return self._render_template(
            'pages/introduction.html',
            {
                'user_instruction_link': WS.get_behaviour_conf(WS.BEHAVIOUR_USER_INSTRUCTION_LINK, self._app),
                'introduction_continue_button': WS.get_text(WS.INTRODUCTION_CONTINUE_BUTTON_LABEL, self._app),
            },
        )
