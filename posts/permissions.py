from rest_framework import permissions

class CustomReadOnly(permissions.BasePermission):
    #글 조회 : 누구나, 글 생성 : 로그인한 유저, 편집 : 글 작성자
    # def has_object_permission(self, request, view, obj):
    #     if request.user.is_admin:
    #         if request.user == obj.author:
    #             return True
    #         return False
    #     elif request.user.is_authenticated:
    #         if request.user == obj.author:
    #             return True
    #         return False 
    #     else:
    #         return False
    
    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        return request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method == "PATCH":
            if obj.author == request.user:
                return request.user.is_authenticated
            else:
                return request.user.is_staff
        if request.method == "DELETE":
            if obj.author == request.user:
                return request.user.is_authenticated
            else:
                return request.user.is_staff
        return obj.author == request.user 