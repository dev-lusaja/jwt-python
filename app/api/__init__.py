def load_handlers():
    from api.handlres import encode, decode
    handlers = {
        'EncodeHandler': encode.EncodeHandler(),
        'DecodeHandler': decode.DecodeHandler()
    }
    return handlers
