import logging
from channels import Group
from channels.sessions import channel_session
from channels.auth import channel_and_http_session_user_from_http

logger = logging.getLogger(__name__)


@channel_and_http_session_user_from_http
def websocket_connect(message):
    logger.info("websocket_connect. message = %s", message)
    Group("notifications").add(message.reply_channel)


@channel_session
def websocket_keepalive(message):
    logger.info("websockett keepalive. message = %s", message)
    Group("notifications").add(message.reply_channel)


@channel_session
def websocket_disconnet(message):
    logger.info("websocket_disconnet. message = %s", message)
    Group("notifications").discard(message.reply_channel)
