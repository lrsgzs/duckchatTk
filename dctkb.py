from tkinter import Tk
from tkwebview2.tkwebview2 import WebView2
from easygui import buttonbox

while True:
    #选择一个鸭信
    xz = buttonbox(
        msg="请选择你要用的鸭信：",
        title="选择一个鸭信",
        choices=["阳光工作室鸭信","LRS鸭信","退出"]
        )
    #判断内容及退出
    if xz == "阳光工作室鸭信":
        we = "http://chat.yangguang-gongzuoshi.top"
    elif xz == "LRS鸭信":
        we = "http://lrsgzs.free.svipss.top/"
    else:
        break
    #初始化
    main = Tk()
    main.title('浏览器')
    main.geometry("500x500+10+10")
    main.iconbitmap("./favicon.ico")
    #web组件
    web = WebView2(main,1440,850)
    web.load_url(we)
    web.pack(side='left')
    #运行窗口
    main.mainloop()
