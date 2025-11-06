import http.server
import socketserver

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"服务器运行在端口 {PORT}")
    print(f"访问 http://localhost:{PORT} 查看网站")
    httpd.serve_forever()    