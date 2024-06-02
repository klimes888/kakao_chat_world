import re
from venv import logger


def parse_text_dto(text):
    if text[0] != "/":
        return None

    # 대괄호 안의 텍스트 추출
    pattern = r"\[(.*?)\]"
    match = re.search(pattern, text)

    if not match:
        return None

    inner_text = match.group(1)

    # key-value 쌍을 추출하고 공백을 트림
    params = dict(re.findall(r"(\w+)\s*=\s*([^,]+)", inner_text))
    params = {k: v.strip() for k, v in params.items()}

    # WorldDto 객체 생성
    name = params.get("이름", None)
    desc = params.get("설명", None)
    image_url = params.get("이미지", None)

    return {"name": name, "desc": desc, "image_url": image_url}
