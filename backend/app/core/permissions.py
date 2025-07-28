from enum import Enum


class PermissionLevel(Enum):
    READ = 1      # 조회만 가능
    WRITE = 2     # 조회 + 편집 가능
    DELETE = 3    # 조회 + 편집 + 삭제 가능
    SUPER = 9     # 모든 권한


def check_permission(user_level: int, required_level: PermissionLevel) -> bool:
    """사용자 권한 확인"""
    return user_level >= required_level.value


class UserType(Enum):
    SUPER_ADMIN = "super_admin"
    EVENT_MANAGER = "event_manager"
    PUBLIC = "public"
