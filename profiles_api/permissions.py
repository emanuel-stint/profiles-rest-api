from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to only edit their own profiles"""

    def has_object_permission(self, request, view, obj):
        """check user is trying to edit their own profile"""
        # safe method is like get - read only, whereas updates are not safe methods
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOwnFeed(permissions.BasePermission):
    """allow users to only update their own feed"""

    def has_object_permission(self, request, view, obj):
        """check user is trying to update their own feed"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
