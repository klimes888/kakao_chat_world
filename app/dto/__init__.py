import re
import logging

logger = logging.getLogger(__name__)


def parse_text_dto(text):
    # 입력 텍스트에서 줄바꿈 문자 제거
    text = text.replace("\n", "")

    if text[0] != "[" or text[-1] != "]":
        return None

    # 대괄호 안의 텍스트 추출
    inner_text = text[1:-1]  # 대괄호 제거

    # key-value 쌍을 추출하고 공백을 트림
    params = dict(re.findall(r"(\w+)\s*=\s*([^,]+)", inner_text))
    params = {k: v.strip() for k, v in params.items()}
    # WorldDto 객체 생성
    name = params.get("이름", None)
    user = params.get("유저", None)
    desc = params.get("설명", None)
    image_url = params.get("이미지", None)

    return {"name": name, "desc": desc, "image_url": image_url, "user": user}
