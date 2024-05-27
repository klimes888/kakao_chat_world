from enum import Enum


class UserRole(Enum):
    SUPER_ADMIN = 1  # root
    ADMIN = 2  # 관리자
    SUB_ADMIN = 3  # 부관리자
    USER = 4  # 일반 사용자


class SubContentType(Enum):
    NONE = 0
    ECONOMIC = 1  # 경제
    DEFENSE = 2  # 국방
    POLITICAL = 3  # 정치
    SOCIAL = 4  # 사회
    CULTURE = 5  # 문화
    EDUCATION = 6  # 교육
    ENVIRONMENT = 7  # 환경
    SCIENCE = 8  # 과학
    HUMANITY = 9  # 인문


class ForceDefenseType(Enum):
    NONE = 0
    # 육군
    ARMY = 1
    # 해군
    NAVY = 2
    # 공군
    AIR_FORCE = 3
    # 해병대
    MARINE_CORPS = 4
    # 우주군
    SPACE_FORCE = 5


# 무기 장비
class WeaponType(Enum):
    NONE = 0
    TANK = 1  # 전차
    ARMORED_CAR = 2  # 장갑차
    SELF_PROPELLED_ARTILLERY = 3  # 자주포
    ROCKET_ARTILLERY = 4  # 로켓포
    INFANTRY_FIGHTING_VEHICLE = 5  # 보병 전투차량
    FIGHTER = 10  # 공격기
    BOMBER = 11  # 폭격기
    TRANSPORT_PLANE = 12  # 수송기
    COMBAT_PLANE = 13  # 전투기
    ATTACK_HELICOPTER = 20  # 공격 헬기
    TRANSPORT_HELICOPTER = 21  # 수송 헬기
    HIGH_SPEED_BOAT = 30  # 고속정/함
    SUBMARINE = 31  # 잠수함
    PATROL_BOAT = 32  # 초계함
    ESCORT_SHIP = 33  # 호위함
    DESTROYER = 34  # 구축함
    CRUISER = 35  # 순양함
    BATTLESHIP = 36  # 전함
    AIRCRAFT_CARRIER = 37  # 항공모함
    LANDING_SHIP = 38  # 상륙함
    HELICOPTER_CARRIER = 39  # 헬기 모함
    RECONNAISSANCE_SATELLITE = 50  # 정찰 위성
    DEFENSE_SATELLITE = 51  # 방어 위성
    ATTACK_SATELLITE = 52  # 공격 위성
    SPACE_STATION = 53  # 우주 정거장
