from roles import UserRole
from permissions import Permission


class User:
    def __init__(self, user_id: str, roles: set[UserRole]):
        self.user_id = user_id
        self.roles = roles


class PermissionSystem:
    def __init__(self):
        self.role_permissions: dict[UserRole, Permission] = {
            UserRole.GUEST: Permission.VIEW_PUBLIC | Permission.REPORT_CONTENT,
            UserRole.REGULAR: (
                Permission.VIEW_PUBLIC |
                Permission.VIEW_PRIVATE |
                Permission.CHAT_PUBLIC |
                Permission.CHAT_PRIVATE |
                Permission.EDIT_OWN_PROFILE |
                Permission.USE_CUSTOM_EMOJIS |
                Permission.REPORT_CONTENT
            ),
            UserRole.COMMUNITY_FOUNDER: (
                Permission.VIEW_PUBLIC |
                Permission.VIEW_PRIVATE |
                Permission.CHAT_PUBLIC |
                Permission.CHAT_PRIVATE |
                Permission.CREATE_COMMUNITY |
                Permission.DELETE_COMMUNITY |  # Added this permission
                Permission.EDIT_COMMUNITY_SETTINGS |
                Permission.INVITE_USERS |
                Permission.REMOVE_USERS |
                Permission.MUTE_USERS |
                Permission.EDIT_COMMUNITY_RULES |
                Permission.CREATE_COMMUNITY_RULES |  # Added this permission
                Permission.PIN_CHATS |
                Permission.MANAGE_ROLES |
                Permission.AWARD_BADGES |
                Permission.REVOKE_BADGES |
                Permission.EXPORT_CHAT_HISTORY |
                Permission.VIEW_ANALYTICS  # Added this permission
            ),
            UserRole.COMMUNITY_MANAGER: (
                Permission.VIEW_PUBLIC |
                Permission.VIEW_PRIVATE |
                Permission.CHAT_PUBLIC |
                Permission.CHAT_PRIVATE |
                Permission.EDIT_COMMUNITY_SETTINGS |
                Permission.INVITE_USERS |
                Permission.REMOVE_USERS |  # Added this permission
                Permission.MUTE_USERS |  # Added this permission
                Permission.MANAGE_ROLES |
                Permission.VIEW_ANALYTICS |
                Permission.EDIT_COMMUNITY_RULES |  # Changed from DELETE to EDIT
                Permission.CREATE_COMMUNITY_RULES |  # Added this permission
                Permission.AWARD_BADGES |  # Added this permission
                Permission.REVOKE_BADGES |
                Permission.PIN_CHATS |  # Added this permission
                Permission.DELETE_COMMUNITY_MESSAGES |  # Added this permission
                Permission.REVIEW_REPORTS  # Added this permission
            ),
            UserRole.MODERATOR: (
                Permission.VIEW_PUBLIC |
                Permission.VIEW_PRIVATE |
                Permission.CHAT_PUBLIC |
                Permission.CHAT_PRIVATE |
                Permission.DELETE_COMMUNITY_MESSAGES |
                Permission.REMOVE_USERS |
                Permission.MUTE_USERS |
                Permission.REPORT_CONTENT |
                Permission.PIN_CHATS |
                Permission.AWARD_BADGES |
                Permission.REVOKE_BADGES |
                Permission.REVIEW_REPORTS
            ),
            UserRole.COMMUNITY_TRANSLATOR: (
                Permission.VIEW_PUBLIC |
                Permission.VIEW_PRIVATE |
                Permission.CHAT_PUBLIC |
                Permission.CHAT_PRIVATE |
                Permission.TRANSLATE_CHATS
            ),
            UserRole.EMOJI_CURATOR: (
                Permission.VIEW_PUBLIC |
                Permission.VIEW_PRIVATE |
                Permission.CHAT_PUBLIC |
                Permission.CHAT_PRIVATE |
                Permission.CREATE_EMOJIS |
                Permission.DELETE_EMOJIS |
                Permission.SUGGEST_EMOJIS |
                Permission.APPROVE_EMOJIS |
                Permission.USE_CUSTOM_EMOJIS
            ),
            UserRole.TREND_SETTER: (
                Permission.VIEW_PUBLIC |
                Permission.VIEW_PRIVATE |
                Permission.CHAT_PUBLIC |
                Permission.CHAT_PRIVATE |
                Permission.SET_TRENDS
            ),
            UserRole.OVERSEER: Permission(~0)
        }
    
    def get_user_permissions(self, user: User) -> Permission:
        return Permission(sum(self.role_permissions[role] for role in user.roles))
    
    def has_permission(self, user: User, permission: Permission) -> bool:
        return bool(self.get_user_permissions(user) & permission)
    
    def grant_permission(self, role: UserRole, permission: Permission) -> None:
        self.role_permissions[role] |= permission
    
    def revoke_permission(self, role: UserRole, permission: Permission) -> None:
        self.role_permissions[role] &= ~permission
    
    def get_role_permissions(self, role: UserRole) -> Permission:
        return [perm.name for perm in Permission if perm in self.role_permissions[role]]
    
    def add_role_to_user(self, user: User, role: UserRole) -> None:
        user.roles.add(role)
    
    def remove_role_from_user(self, user: User, role: UserRole) -> None:
        user.roles.discard(role)
