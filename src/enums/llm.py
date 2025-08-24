
import enum


class RoleEnum(str, enum.Enum):
    user = "user"
    ai = "ai"
    system = "system"
