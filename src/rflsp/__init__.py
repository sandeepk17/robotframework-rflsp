import uuid

from pygls.features import COMPLETION, TEXT_DOCUMENT_DID_CHANGE, TEXT_DOCUMENT_DID_CLOSE, TEXT_DOCUMENT_DID_OPEN
from pygls.server import LanguageServer
from pygls.types import (
    DidChangeTextDocumentParams,
    DidCloseTextDocumentParams,
    DidOpenTextDocumentParams,
    MessageType,
    Registration,
    RegistrationParams,
    Unregistration,
    UnregistrationParams,
)


class RobotFrameworkLanguageServer(LanguageServer):
    CMD_REGISTER_COMPLETIONS = "registerCompletions"
    CMD_UNREGISTER_COMPLETIONS = "unregisterCompletions"
    CONFIGURATION_SECTION = "rfServer"

    def __init__(self):
        super().__init__()


robot_server = RobotFrameworkLanguageServer()


def _validate(ls, params):
    ls.show_message_log("Robot Framework Validation...")
    text_doc = ls.workspace.get_document(params.textDocument.uri)
    source = text_doc.source  # noqa: F841
    diagnostics = None
    ls.publish_diagnostics(text_doc.uri, diagnostics)


@robot_server.feature(TEXT_DOCUMENT_DID_CHANGE)
def did_change(ls, params: DidChangeTextDocumentParams):
    """Text document did change notification."""
    _validate(ls, params)


@robot_server.feature(TEXT_DOCUMENT_DID_CLOSE)
def did_close(server: RobotFrameworkLanguageServer, params: DidCloseTextDocumentParams):
    """Text document did close notification."""
    server.show_message("Text Document Did Close")


@robot_server.feature(TEXT_DOCUMENT_DID_OPEN)
async def did_open(ls, params: DidOpenTextDocumentParams):
    """Text document did open notification."""
    ls.show_message("Text Document Did Open")
    _validate(ls, params)


@robot_server.command(RobotFrameworkLanguageServer.CMD_REGISTER_COMPLETIONS)
async def register_completions(ls: RobotFrameworkLanguageServer, *args):
    """Register completions method on the client."""
    params = RegistrationParams([Registration(str(uuid.uuid4()), COMPLETION, {"triggerCharacters": "[':']"})])
    response = await ls.register_capability_async(params)
    if response is None:
        ls.show_message("Successfully registered completions method")
    else:
        ls.show_message("Error happened during completions registration.", MessageType.Error)


@robot_server.command(RobotFrameworkLanguageServer.CMD_UNREGISTER_COMPLETIONS)
async def unregister_completions(ls: RobotFrameworkLanguageServer, *args):
    """Unregister completions method on the client."""
    params = UnregistrationParams([Unregistration(str(uuid.uuid4()), COMPLETION)])
    response = await ls.unregister_capability_async(params)
    if response is None:
        ls.show_message("Successfully unregistered completions method")
    else:
        ls.show_message("Error happened during completions unregistration.", MessageType.Error)
