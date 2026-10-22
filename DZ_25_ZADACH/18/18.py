import json
import logging
import re
from collections import Counter

logging.basicConfig(
    filename="processing.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

pattern=re.compile(
    r"^\S+\s+\S+\s+(?P<ip>\S+)\s+(?P<method>GET|POST|PUT|DELETE|PATCH)\s+(?P<url>\S+)\s+(?P<status>\d{3})$"
)

methods=Counter()
urls=Counter()
errors=0

try:
    logging.info("Начало обработки")

    with open("access.log","r",encoding="utf-8") as file:
        for line in file:
            line=line.strip()

            match=pattern.match(line)

            if not match:
                logging.warning("Некорректная строка")
                continue

            data=match.groupdict()

            method=data["method"]
            url=data["url"]
            status=int(data["status"])

            methods[method]+=1
            urls[url]+=1

            if 400<=status<500:
                errors+=1

    if urls:
        most_frequent_url=urls.most_common(1)[0][0]
    else:
        most_frequent_url=None

    result={
        "requests_by_method":dict(methods),
        "errors_4xx":errors,
        "most_frequent_url":most_frequent_url
    }

    with open("statistics.json","w",encoding="utf-8") as file:
        json.dump(result,file,ensure_ascii=False,indent=4)

    logging.info("Обработка завершена")

except FileNotFoundError:
    print("Файл не найден")
    logging.error("Файл access.log не найден")

except PermissionError:
    print("Нет доступа к файлу")
    logging.error("Нет доступа к access.log")

except OSError as error:
    print("Ошибка:",error)
    logging.error("Ошибка ОС: %s",error)
