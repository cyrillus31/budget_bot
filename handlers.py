def help_message_handler(update_id, last_update, message) -> str:
    if update_id != last_update  and message == "hi":
        return "HELLO THERE! NEED SOME  HEEEELP?"

