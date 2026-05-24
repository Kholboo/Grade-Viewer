#!/usr/bin/env python3
"""
Шалгалтын Анализийн Систем - Локал Сервер
Энэ файлыг exam-analysis.html-тэй ижил хавтаст хадгалаад ажиллуулна уу.
"""
import http.server
import socketserver
import webbrowser
import os

PORT = 8080

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # Консол дахь логийг нуух

os.chdir(os.path.dirname(os.path.abspath(__file__)))

print("=" * 50)
print("  Шалгалтын Анализийн Систем")
print("=" * 50)
print(f"\n✅ Сервер ажиллаж байна: http://localhost:{PORT}")
print("   Браузер автоматаар нээгдэнэ...")
print("\n   Зогсоохын тулд: Ctrl + C\n")

webbrowser.open(f"http://localhost:{PORT}/exam-analysis.html")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\nСервер зогслоо.")
