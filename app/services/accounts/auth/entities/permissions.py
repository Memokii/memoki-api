from enum import IntFlag, auto

class Permission(IntFlag):
    # view permissions
    VIEW_PUBLIC = auto()
    VIEW_PRIVATE = auto()
    VIEW_ANALYTICS = auto()

    # chat permissions
    CHAT_PUBLIC = auto()
    CHAT_PRIVATE = auto()
    EXPORT_CHAT_HISTORY = auto()
    PIN_CHATS = auto()
    TRANSLATE_CHATS = auto()
    REPORT_CONTENT = auto()

    # community permissions
    CREATE_COMMUNITY = auto()
    DELETE_COMMUNITY = auto()
    EDIT_COMMUNITY_SETTINGS = auto()
    DELETE_COMMUNITY_MESSAGES = auto()
    CREATE_COMMUNITY_RULES = auto()
    DELETE_COMMUNITY_RULES = auto()
    EDIT_COMMUNITY_RULES = auto()
    REPORT_COMMUNITY = auto()

    # community user permissions
    INVITE_USERS = auto()
    REMOVE_USERS = auto()
    MUTE_USERS = auto()
    MANAGE_ROLES = auto()

    # emoji permissions
    CREATE_EMOJIS = auto()
    DELETE_EMOJIS = auto()
    SUGGEST_EMOJIS = auto()
    APPROVE_EMOJIS = auto()
    USE_CUSTOM_EMOJIS = auto()

    # badge permissions
    AWARD_BADGES = auto()
    REVOKE_BADGES = auto()

    # profile permissions
    EDIT_OWN_PROFILE = auto()
    ALLOW_OTHERS_TO_EDIT_PROFILE = auto()

    # trend permissions
    SET_TRENDS = auto()
    
    # moderation permissions
    REVIEW_REPORTS = auto()
