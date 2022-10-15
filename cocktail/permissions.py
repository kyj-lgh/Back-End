from rest_framework import permissions

class CustomReadOnly(permissions.BasePermission):
    #글 조회 : 누구나, 글 생성 : 로그인한 유저, 편집 : 글 작성자
    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        return request.user.is_authenticated and request.user.is_admin
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_admin