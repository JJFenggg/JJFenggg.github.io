import qrcode
import os
from PIL import Image, ImageDraw, ImageFont


class QR:
    def __init__(self):
        self.name = input("请输入请假人姓名：")
        self.id_number = input("请输入请假人学号：")
        self.short_long = "短假"  # input("请输入请假类型（短假/长假）：")
        self.false_true = "false"  # input("是否离校（ture/false）：")
        self.reason = "病假"  # input("请输入请假原因：")
        self.describe = "发烧"  # input("请输入原因描述：")
        self.destination = "宿舍"  # input("请输入目的地：")
        self.time = input("请输入开始时间：")
        self.which_class = "3-4 1-2 5-6 7-8 9-11"  # input("请输入节次：")
        self.tutor = "孔瑞；"  # input("请输入审核老师姓名：")
        self.info = [self.name,
                     self.id_number,
                     self.time,]

        self.html_content = f"""
        <!DOCTYPE html>
        <html lang="zh-CN">
        <head>
            <meta charset="utf-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link href="/assets/bootstrap-3.3.7/css/bootstrap.min.css" rel="stylesheet">
            <!-- HTML5 shim 和 Respond.js 是为了让 IE8 支持 HTML5 元素和媒体查询（media queries）功能 -->
            <!-- 警告：通过 file:// 协议（就是直接将 html 页面拖拽到浏览器中）访问页面时 Respond.js 不起作用 -->
            <!--[if lt IE 9]>
            <script src="/assets/html5shiv.min.js"></script>
            <script src="/assets/respond.min.js"></script>
            <![endif]-->
            <style>
                h3 {{
                    color: #333;
                }}
                table {{
                    width:90vw;
                    /* border-left:#C8B9AE solid 1px;
                    border-top:#C8B9AE solid 1px; */
                    /* border: #dad3d2 solid 1px; */
                    border: #e3e3e3 solid 1px;
                    box-shadow: 5px 5px 16px #c7c5c5;
                    margin: 0 auto;
                    border-collapse:collapse;
                    text-align: center;
                }}
        
                /* table thead tr th {{
                    padding: 5px 20px;
                    background-color: blue;
                    font-weight: 400;
                    color: #fff;
                    border-right:#C8B9AE solid 1px;
                    border-bottom:#C8B9AE solid 1px;
                }} */
        
                table tbody tr td {{
                    /*padding: 5px 20px;*/
                    /*border-top: 1px solid blue;*/
                    /* border-right:#C8B9AE solid 1px;
                    border-bottom:#C8B9AE solid 1px; */
                    /* padding:10px 10px 6px; */
                    padding: 1vh 2vw;
                }}
                table tbody tr th {{
                    width: 20vw;
                    color: #212121;
                    padding: 1vh 2vw;
                }}
        
                table tbody tr:nth-child(2n) td {{
                    /* background-color: lightblue; */
                    background-color: rgb(245 240 240);
                    /* border-right:#C8B9AE solid 1px;
                    border-bottom:#C8B9AE solid 1px; */
                    /* padding:10px 10px 6px; */
                }}
                table tbody tr:nth-child(2n) th {{
                    background-color: rgb(233, 224, 224) ;
                }}
        
        
                table tbody tr:last-child td {{
                    /* border-right:#C8B9AE solid 1px;
                    border-bottom:#C8B9AE solid 1px; */
                    /* padding:10px 10px 6px; */
                }}
            </style>
        </head>
        <body>
        <table rules="all">
            <caption><h3 style="text-align: center">智慧曲园学生假条</h3></caption>
            <!--对表格中的列进行组合，以便对其进行格式化-->
            <colgroup>
                <col span="2" >
        <!--        <col style="background-color:yellow">-->
            </colgroup>
        
            <!--表格主体分组-->
            <tbody>
            <tr>
                <th>请假人</th>
                <td>{self.name}</td>
            </tr>
            <tr>
                <th>学号</th>
                <td>{self.id_number}</td>
            </tr>
            <tr>
                <th>请假类型</th>
                <td>{self.short_long}</td>
            </tr>
            <tr>
                <th>是否离校</th>
                <td>{self.false_true}</td>
            </tr>
            <tr>
                <th>请假原因</th>
                <td>{self.reason}</td>
            </tr>
            <tr>
                <th>原因描述</th>
                <td>{self.describe}</td>
            </tr>
            <tr>
                <th>目的地</th>
                <td>{self.destination}</td>
            </tr>
            <tr>
                <th>开始时间</th>
                <td>{self.time}</td>
            </tr>
            <tr>
                <th>结束时间</th>
                <td></td>
            </tr>
            <tr>
                <th>节次</th>
                <td>{self.which_class}</td>
            </tr>
            <tr>
                <th>审核状态</th>
                <td>审核通过</td>
            </tr>
            <tr>
                <th>审核老师姓名</th>
                <td>{self.tutor}; </td>
            </tr>
            </tbody>
        </table>
        
        
        
        <script type="application/javascript" src="/assets/jquery-1.12.4.js"></script>
        <script type="application/javascript" src="/assets/bootstrap-3.3.7/js/bootstrap.min.js"></script>
        <script type="application/javascript">
        
        </script>
        </body>
        </html>
        """

    # 生成html文件
    def html(self):
        with open(f"./QR/{self.name}.html", "w", encoding="utf-8") as f:
            f.write(self.html_content)

    # 把二维码上传到网页
    def push_qr(self):
        os.system(f"git add ./QR/{self.name}.html")
        os.system("git commit -m 'update'")
        os.system("git push origin main")

    # 生成二维码
    @property
    def qr_image(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=0,
        )
        qr.add_data(f"https://jjfenggg.github.io/fake_application_files/QR/{self.name}.html")
        qr.make(fit=True)
        qrimg = qr.make_image(fill_color="black", back_color="white")
        qrimg = qrimg.resize((390, 390))
        return qrimg


class Pic:
    def __init__(self):
        self.image = Image.open("origin.png")  # 把Image对象实例为image，传入原始图片

    # 修改二维码
    '''
    这里的位置待标定，现在的是随便填的
    '''

    def paste_qr(self, qrimg):
        self.image.paste(qrimg, (446, 1418))

    # 修改文字
    '''
    这里的字体，还有字体大小待标定
    还有要写入的位置待标定
    '''

    def paste_text(self, info):
        # 创建字体实例和ImageDraw实例
        font = ImageFont.truetype(font="苹方.ttf", size=48)
        draw = ImageDraw.Draw(self.image)
        # 开始写入
        name, id_number, time = info
        draw.text((403, 410), name, font=font, fill="black")
        draw.text((403, 483), id_number, font=font, fill="black")
        draw.text((403, 915), time, font=font, fill="black")

    def save(self, filename):
        with open(f"./application/{filename}.png", "wb") as f:
            self.image.save(f)


def main():
    qr = QR()
    application = Pic()  # 此处图片待补充
    print("正在写入html...\n")
    qr.html()
    print("正在生成网页...\n")
    qr.push_qr()
    print("正在写入文本数据...\n")
    application.paste_text(qr.info)
    print("正在写入二维码...\n")
    application.paste_qr(qr.qr_image)
    application.save(qr.name)
    print("保存成功！\n 请在application目录下查看您的假假条")


if __name__ == '__main__':
    main()
