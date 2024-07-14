def error_message_handler(messages_error):
    single_message = ""

    for i, msg_error in enumerate(messages_error):
        single_message += f'{msg_error}, '

    single_message = single_message.strip()
    # to dont display the last comma
    single_message = single_message[:len(single_message)-1]

    return single_message