"""切割 tg history json 文件 为较小的多个文件"""

import decimal
import pathlib
import ijson
import json
from loguru import logger

whole_file_path = pathlib.Path(__file__).resolve().parent / "result.json"

file_count = 1

group_title = ""
group_type = ""
group_id = 0


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)


messages = ijson.items(open(whole_file_path, encoding="utf-8"), "messages.item")
message_count = 0
message_list = []
for message in messages:
    if message["id"] < 0:
        continue
    message_count += 1
    message_list.append(message)
    if message_count % 16000 == 0:
        logger.info(f"message count: {message_count}, creating file {file_count}")
        data = {
            "name": group_title,
            "type": group_type,
            "id": group_id,
            "messages": message_list,
        }
        with open(f"result_{file_count}.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4, cls=DecimalEncoder)
        logger.info(f"file {file_count} done")
        file_count += 1
        message_list = []

logger.info(f"total message count: {message_count}")

if message_list:
    logger.info(f"creating file {file_count}")
    data = {
        "name": group_title,
        "type": group_type,
        "id": group_id,
        "messages": message_list,
    }
    with open(f"result_{file_count}.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4, cls=DecimalEncoder)
    logger.info(f"file {file_count} done")
