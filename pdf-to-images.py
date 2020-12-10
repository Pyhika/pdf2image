import os
import re
from pathlib import Path
from pdf2image import convert_from_path

# poppler/binを環境変数Pathに追加
poppler_dir = Path(__file__).parent.absolute() / "poppler/bin"
os.environ["PATH"] += os.pathsep + str(poppler_dir)

# PDFファイルのパス
path = './pdf_files/'
files = []
for filename in os.listdir(path):
    if os.path.isfile(os.path.join(path, filename)):
        files.append(filename)

# 正規表現にてPDFのみを処理する
pdf_files = []
regex = re.compile(r'(.pdf)$')
for num, name in enumerate(files):
    if regex.search(name):
        pdf_files.append(name)

# # PDF -> Image　に変換(150dpi)
        pdf_path = Path("./pdf_files/" + pdf_files[num - 1])
        pages = convert_from_path(pdf_path, 150)

# 画像ファイルを１ページずつ保存
        image_dir = Path("./image_files")
        for i, page in enumerate(pages):
            file_name = pdf_path.stem + "_{:03d}".format(i + 1) + ".jpeg"
            image_path = image_dir / file_name
            # JPEGで保存
            page.save(str(image_path), "JPEG")

# jpegファイルを種類ごとに仕分ける
os.chdir("./image_files")
files = os.listdir()
for file in files:
    # Mac用↓↓
    os.renames(file, file[:-8]+"/"+file)
    # Windows用↓↓
    # os.renames(file, file[:-8]+"\\"+file)
