import pyqrcode
# from pyqrcode import QRCode

code = pyqrcode.create("ruben dario gacha castelblanco")
code.svg("code.svg",scale=9) 