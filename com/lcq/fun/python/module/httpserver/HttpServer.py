#/usr/bin/python3
# -*- coding: UTF-8 -*-

from http.server import  BaseHTTPRequestHandler,HTTPServer
from os import  path
from urllib.parse import  urlparse
import  json
import  zipfile
import  os
import  time

# 使用httpServer库启动服务，接收请求并响应。相对于Java来说方便很多
class downloadRelease(BaseHTTPRequestHandler):

    def zip_ya(self,startdir,file_news):

        z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)  # 参数一：文件夹名

        for dirpath, dirnames, filenames in os.walk(startdir):
            fpath = dirpath.replace(startdir, '')  # 这一句很重要，不replace的话，就从根目录开始复制
            fpath = fpath and fpath + os.sep or ''  # 这句话理解我也点郁闷，实现当前文件夹以及包含的所有文件的压缩
            for filename in filenames:
                z.write(os.path.join(dirpath, filename), fpath + filename)
                print('压缩成功')

        z.close()

    def do_GET(self):
        queryPath = urlparse(self.path)
        filepath,query = queryPath.path,queryPath.query

        if(filepath == '/downloadlib'):
            print("downloadlib start,version="+query)

            self.send_response(200)
            self.send_header("Content-type","multipart/form-data")

            curr = time.strftime("%Y%m%d%H-%M:%S", time.localtime())
            filename = curr+"releases.zip"


            self.send_header("Content-Disposition","attachment;filename="+filename)
            self.end_headers()

            startdir = "/Users/chaoqunluo/Documents/temp/rel"
            file_news = "/Users/chaoqunluo/Documents/temp/"+filename

            self.zip_ya(startdir,file_news);
            f = open(file_news,"rb")
            self.wfile.write(f.read());
            self.wfile.flush()
            f.close()
            #os.remove(file_news)
            return ;

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("<center><img src='http://localhost:9091/2.jpeg' /></center>".encode('utf-8'))

def run():
    port = 8082
    print("starting downloadRelease server ,port=",port)

    server_address = ('',port);
    httpd = HTTPServer(server_address,downloadRelease)
    print("running server .....")
    httpd.serve_forever()

if __name__ == '__main__':
    run()








