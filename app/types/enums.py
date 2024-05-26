from enum import Enum


class UserRole(Enum):
    SUPER_ADMIN = 1  # root
    ADMIN = 2  # 관리자
    SUB_ADMIN = 3  # 부관리자
    USER = 4  # 일반 사용자
