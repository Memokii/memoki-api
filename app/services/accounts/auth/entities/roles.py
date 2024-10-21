from enum import Enum

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
