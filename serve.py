# -*- coding: utf-8 -*-
"""
徐梓轩课堂实践 - 本地 HTTP 服务器
功能：
  1. 静态文件服务（所有 html / css / img 等）
  2. GET /files          → 返回目录下所有 .html 文件，按 mtime 升序（越旧越靠前）
  3. GET /check-update   → 返回所有文件的最新 mtime（用于热更新轮询）

访问：http://localhost:8000/
"""
import os
import json
import time
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXCLUDE = {'index.html', 'serve.py'}


def scan_html():
    """扫描目录下所有 .html 文件，返回 [(name, ctime), ...]，按 ctime 升序（越旧越靠前）"""
    items = []
    for name in os.listdir(BASE_DIR):
        if not name.lower().endswith('.html'):
            continue
        if name in EXCLUDE:
            continue
        full = os.path.join(BASE_DIR, name)
        if os.path.isfile(full):
            # Windows 上 getctime = 创建时间，getmtime = 修改时间
            ctime = int(os.path.getctime(full))
            items.append((name, ctime))
    # 按创建时间升序 → 先创建的排在前面
    items.sort(key=lambda x: x[1])
    return items


class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        path = urlparse(self.path).path

        if path == '/files':
            items = scan_html()
            data = {name: mtime for name, mtime in items}
            body = json.dumps(data, ensure_ascii=False).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Cache-Control', 'no-store')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        if path == '/check-update':
            # 热更新需要用 mtime（任何修改都能触发）
            latest = 0
            files_ctime = {}
            for name, _ in scan_html():
                full = os.path.join(BASE_DIR, name)
                mtime = int(os.path.getmtime(full))
                ctime = int(os.path.getctime(full))
                files_ctime[name] = ctime
                if mtime > latest:
                    latest = mtime
            body = json.dumps({'latest': latest, 'files': files_ctime}).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Cache-Control', 'no-store')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        # 默认：静态文件服务
        super().do_GET()

    def log_message(self, fmt, *args):
        t = time.strftime('%H:%M:%S')
        print(f"[{t}] {args[0]}")


if __name__ == '__main__':
    port = 8000
    os.chdir(BASE_DIR)
    server = HTTPServer(('0.0.0.0', port), Handler)
    print(f"\n  徐梓轩课堂实践 - 本地服务器已启动")
    print(f"  访问地址: http://localhost:{port}/")
    print(f"  项目目录: {BASE_DIR}\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n  服务器已停止")
        server.server_close()
