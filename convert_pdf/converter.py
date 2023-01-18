from fpdf import FPDF
import os
import io
import base64
import numpy as np
from PIL import Image
from all_testing.image_test import image_base
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate


class PDF2MAIL(FPDF):

    def __init__(self, response, email):
        self.response = response
        self.email = email

    def base2pdf(self, image_base):
        img = Image.open(io.BytesIO(base64.decodebytes(bytes(image_base, "utf-8"))))
        rand = np.random.randint(1, 1000)
        image_name = r'D:\projectImg2Color\convert_pdf\temp\temp{}.jpeg'.format(rand)
        img.save(image_name)
        pdf = FPDF()
        pdf.add_page()
        pdf.image(image_name)
        pdf_name = r'D:\projectImg2Color\convert_pdf\temp\temp{}.pdf'.format(rand)
        pdf.output(pdf_name, 'F')
        self.send_mail('ryabukhin_nikita@mail.ru', [self.email], 'img2color', 'Ready your image!', files=[pdf_name])
        os.remove(pdf_name)
        os.remove(image_name)

    def send_mail(self, send_from, send_to, subject, text, files=None, server="127.0.0.1"):
            assert isinstance(send_to, list)

            msg = MIMEMultipart()
            msg['From'] = send_from
            msg['To'] = COMMASPACE.join(send_to)
            msg['Date'] = formatdate(localtime=True)
            msg['Subject'] = subject

            msg.attach(MIMEText(text))

            for f in files or []:
                with open(f, "rb") as fil:
                    part = MIMEApplication(
                        fil.read(),
                        Name=basename(f)
                    )
                # After the file is closed
                part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
                msg.attach(part)

            smtp = smtplib.SMTP('smtp.gmail.com', 587)
            smtp.starttls()
            smtp.login('riabukhin.nikita@gmail.com', 'password')
            smtp.sendmail(send_from, send_to, msg.as_string())
            smtp.close()

    def pdf2mail(self):
        for key, value in self.response.items():
            for img_key, image_value in value.items():
                self.base2pdf(image_base=image_value)


if __name__ == '__main__':
    p = PDF2MAIL(image_base, email='ryabukhin_nikita@mail.ru')
    print(p.base2pdf(image_base=image_base))
