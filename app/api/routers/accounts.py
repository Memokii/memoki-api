"""
/accounts/generate
    - /username GET: Generate a username
    - /avatar GET: Generate an avatar

/accounts/users
    - / POST: Create a new user
    - /<user_id> GET: Retrieve a user
    - /<user_id> PUT: Update a user
    - /<user_id> DELETE: Delete a user

    - /<user id>/onboarding POST: Onboard a user

    - /<user id>/devices POST: Add a device to a user
    - /<user id>/devices/<device hash> GET: Retrieve a device
    - /<user id>/devices/<device hash> DELETE: Remove a device from a user

/accounts/communities
    - / POST: Create a new community
    - /search GET: Search for communities (with filters)
    - /<community_id> GET: Retrieve a community
    - /<community_id> PUT: Update a community
    - /<community_id> DELETE: Delete a community
    - /<community_id>/members GET: Retrieve a list of members in a community
    - /<community_id>/invitations GET: Retrieve a list of invitations to a community
    - /<community_id>/invitations POST: Invite a user to a community
    - /<community_id>/invitations/<invitation_id> DELETE: Remove an invitation to a community
"""

from fastapi import APIRouter


class Accounts:
    def __init__(self):
        self.__router = APIRouter(
            prefix="/accounts",
            tags=["accounts"]
        )

        self.__generate_router()
        self.__users_router()
        self.__communities_router()
    
    def __generate_router(self):
        pass

    def __users_router(self):
        pass

    def __communities_router(self):
        pass

    @property
    def router(self):
        return self.__router
