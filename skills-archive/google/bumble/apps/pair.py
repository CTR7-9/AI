class Delegate(PairingDelegate):
    def __init__(self, mode, connection, capability_string, do_prompt):
        super().__init__(
            io_capability={
                'keyboard': PairingDelegate.KEYBOARD_INPUT_ONLY,
                'display': PairingDelegate.DISPLAY_OUTPUT_ONLY,
                'display+keyboard': PairingDelegate.DISPLAY_OUTPUT_AND_KEYBOARD_INPUT,
                'display+yes/no': PairingDelegate.DISPLAY_OUTPUT_AND_YES_NO_INPUT,
                'none': PairingDelegate.NO_OUTPUT_NO_INPUT,
            }[capability_string.lower()]
        )

    async def prompt(self, message):
        # Wait a bit to allow some of the log lines to print before we prompt
        await asyncio.sleep(1)

        session = PromptSession(message)
        response = await session.prompt_async()
        return response.lower().strip()

(Excerpted from google/bumble/apps/pair.py)
