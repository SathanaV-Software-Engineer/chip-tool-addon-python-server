FROM python:3.11-alpine

WORKDIR /app

COPY chip_tool_server.py /app/
COPY run.sh /app/
RUN chmod +x /app/run.sh

RUN pip install flask flask-cors

EXPOSE 6000

CMD ["/app/run.sh"]
