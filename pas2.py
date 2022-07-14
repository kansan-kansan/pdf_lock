from PyPDF2 import PdfFileWriter, PdfFileReader

pas = str(input("set up pas>>"))
#befor_dir = str(input("施錠するpdfのディレクトリ>>"))
#PdfFileWriterオブジェクトを作成
out = PdfFileWriter()

'''
13行目のディレクトリを変数に変えたい
↓
Tkinterで実装
'''

#指定したPDFファイルをPdfFileReaderで開く
file = PdfFileReader(r"C:\Users\ayume\Desktop\free\アプリ開発\pas_ロック\1_2.pdf")

#PDFファイルのページ数を取得する
num = file.numPages

#PDFファイルの全ページを繰り返し、ファイル作成
#新しいファイルにページを追加する
for idx in range(num):
    page = file.getPage(idx)
    out.addPage(page)

#パスワードを設定
password  = pas

#入力したパスワードで新しいファイルを暗号化
out.encrypt(password)
after_name = str(input("file name>>"))
#新しいPDFファイルを作成
#暗号化された情報をファイルに書き込み
with open(after_name+".pdf","wb") as f:
    out.write(f)