from enum import Enum

class Permissions(int, Enum):
    VIEW_PUBLIC = 1 << 0
    VIEW_PRIVATE = 1 << 1
    CHAT_PUBLIC = 1 << 2
    CHAT_PRIVATE = 1 << 3
    CREATE_COMMUNITY = 1 << 4
    DELETE_COMMUNITY = 1 << 5
    EDIT_COMMUNITY_SETTINGS = 1 << 6
    INVITE_USERS = 1 << 7
    REMOVE_USERS = 1 << 8
    MUTE_USERS = 1 << 9
    DELETE_COMMUNITY_MESSAGES = 1 << 10
    PIN_MESSAGES = 1 << 11
    CREATE_EMOJIS = 1 << 12
    DELETE_EMOJIS = 1 << 13
    SUGGEST_EMOJIS = 1 << 14
    APPROVE_EMOJIS = 1 << 15
    USE_CUSTOM_EMOJIS = 1 << 16
    CREATE_COMMUNITY_RULES = 1 << 17
    DELETE_COMMUNITY_RULES = 1 << 18
    EDIT_COMMUNITY_RULES = 1 << 19
    SET_TRENDS = 1 << 20
    AWARD_BADGES = 1 << 21
    REVOKE_BADGES = 1 << 22
    TRANSLATE_MESSAGES = 1 << 23
    EDIT_OWN_PROFILE = 1 << 24
    ALLOW_OTHERS_TO_EDIT_PROFILE = 1 << 25
    VIEW_ANALYTICS = 1 << 26
    EXPORT_CHAT_HISTORY = 1 << 27
    REPORT_COMMUNITIES = 1 << 28
    REVIEW_REPORTS = 1 << 29
    MANAGE_ROLES = 1 << 30


class UserRole(str, Enum):
    GUEST = 'guest' # has limited access to the platform e.g. can only mostly view public communities' most recent messages
    REGULAR = 'regular' # can view and chat in public or private communities
    COMMUNITY_FOUNDER = 'community_founder' # can maange and moderate a community, but cannot delete it e.g. a community creator
    COMMUNITY_MANAGER = 'community_manager' # can manage a community but doesn't have the ability to moderate it e.g. change settings, invite users
    COMMUNITY_TRANSLATOR = 'community_translator' # can do emoji-to-text translations to help onboard new members
    EMOJI_CURATOR = 'emoji_curator' # can create, delete, suggest, approve, and test in-development emojis
    TREND_SETTER = 'trend_setter' # can start trends for communities simultaneously e.g. starting a conversation about a trending topic
    MODERATOR = 'moderator' # can moderate a community but doesn't have the ability to manage it e.g. delete messages, mute users
    OVERSEER = 'overseer' # doesn't interact with the platform but can manage all its entities e.g. a parent company
