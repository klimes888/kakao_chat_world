codes = {
    "0000": "세계를 성공적으로 생성했습니다!\n[세계명]: {0}\n[관리자]: {1}\n[설명]: {2}",
    "0001": "이미 유저나 세계가 존재합니다",
    "0002": "다시 한번 시도해주세요",
}


def get_code(code: str):
    return codes[code] if code in codes else "unknown code"
