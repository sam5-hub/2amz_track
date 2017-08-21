import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from datetime import datetime
from tool.file_deal import make_resource_zip, settings

today = datetime.now().strftime('%y-%m-%d')
resource_path = settings.attributes.get('IMAGES_STORE').value


class Mailer(object):
    def __init__(self, maillist, mailtitle, mailcontent):
        self.mail_list = maillist
        self.mail_title = mailtitle
        self.mail_content = mailcontent

        self.mail_host = "smtp.163.com"
        self.mail_user = "13286826558@163.com"
        self.mail_pass = "AAkobe2413"
        self.mail_postfix = "163.com"

    def sendMail(self):

        me = self.mail_user + "<" + self.mail_user + "@" + self.mail_postfix + ">"
        msg = MIMEMultipart()
        msg['Subject'] = 'Amazon每日更新 - ' + today
        msg['From'] = me
        msg['To'] = ";".join(self.mail_list)

        # puretext = MIMEText('<h1>你好，<br/>'+self.mail_content+'</h1>','html','utf-8')
        puretext = MIMEText('图片资源' + self.mail_content)
        msg.attach(puretext)

        # zip类型的附件
        zip_dir = make_resource_zip(resource_path)
        zippart = MIMEApplication(open(zip_dir, 'rb').read())
        zippart.add_header('Content-Disposition', 'attachment', filename=today + '.zip')
        msg.attach(zippart)

        # pdf类型附件
        # part = MIMEApplication(open('foo.pdf', 'rb').read())
        # part.add_header('Content-Disposition', 'attachment', filename="foo.pdf")
        # msg.attach(part)

        try:
            s = smtplib.SMTP()  # 创建邮件服务器对象
            s.connect(self.mail_host)  # 连接到指定的smtp服务器。参数分别表示smpt主机和端口
            s.login(self.mail_user, self.mail_pass)  # 登录到你邮箱
            s.sendmail(me, self.mail_list, msg.as_string())  # 发送内容
            s.close()
            return True
        except Exception as e:
            print(str(e))
            return False

def send_amz_mail():
    mailto_list = ["iamkeason@gmail.com",'343935669@qq.com']
    mail_title = 'Amazon每日更新 - ' + today
    mail_content = 'Amazon每日更新 - ' + today
    mm = Mailer(mailto_list, mail_title, mail_content)
    res = mm.sendMail()
    print('邮件发送成功' + res)


