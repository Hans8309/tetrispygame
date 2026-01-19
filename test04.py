"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
import random
from tkinter import *
from tkinter.ttk import *
class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_frame_m0t2kgpo = self.__tk_frame_m0t2kgpo(self)
        self.tk_label_m0t2kqaf = self.__tk_label_m0t2kqaf( self.tk_frame_m0t2kgpo) 
        self.tk_input_m0t2kvni = self.__tk_input_m0t2kvni( self.tk_frame_m0t2kgpo) 
        self.tk_button_m0t2kyjw = self.__tk_button_m0t2kyjw( self.tk_frame_m0t2kgpo) 
        self.tk_button_m0t2l0z9 = self.__tk_button_m0t2l0z9( self.tk_frame_m0t2kgpo) 
        self.tk_frame_m0t2le6k = self.__tk_frame_m0t2le6k(self)
        self.tk_text_m0t2lo9i = self.__tk_text_m0t2lo9i( self.tk_frame_m0t2le6k) 
        self.tk_progressbar_m0t2lrxa = self.__tk_progressbar_m0t2lrxa( self.tk_frame_m0t2le6k) 
        self.tk_check_button_m0t2lvon = self.__tk_check_button_m0t2lvon( self.tk_frame_m0t2le6k) 
        self.tk_radio_button_m0t2m2qb = self.__tk_radio_button_m0t2m2qb( self.tk_frame_m0t2le6k) 
        self.tk_radio_button_m0t2m5u0 = self.__tk_radio_button_m0t2m5u0( self.tk_frame_m0t2le6k) 
        self.tk_check_button_m0t2matm = self.__tk_check_button_m0t2matm( self.tk_frame_m0t2le6k) 
        self.tk_label_frame_m0t2mle2 = self.__tk_label_frame_m0t2mle2(self)
        self.tk_check_button_m0t2mzao = self.__tk_check_button_m0t2mzao( self.tk_label_frame_m0t2mle2) 
        self.tk_check_button_m0t2n1gt = self.__tk_check_button_m0t2n1gt( self.tk_label_frame_m0t2mle2) 
        self.tk_check_button_m0t2n3mm = self.__tk_check_button_m0t2n3mm( self.tk_label_frame_m0t2mle2) 
        self.tk_select_box_m0t2n6rv = self.__tk_select_box_m0t2n6rv( self.tk_label_frame_m0t2mle2) 
        self.tk_scale_m0t2ng1s = self.__tk_scale_m0t2ng1s( self.tk_label_frame_m0t2mle2) 
        self.tk_button_m0t2nl04 = self.__tk_button_m0t2nl04( self.tk_label_frame_m0t2mle2) 
    def __win(self):
        self.title("Tkinter布局助手")
        # 设置窗口大小、居中
        width = 600
        height = 500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        
        self.resizable(width=False, height=False)
        
    def scrollbar_autohide(self,vbar, hbar, widget):
        """自动隐藏滚动条"""
        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)
        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)
        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())
    
    def v_scrollbar(self,vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')
    def h_scrollbar(self,hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')
    def create_bar(self,master, widget,is_vbar,is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)
    def __tk_frame_m0t2kgpo(self,parent):
        frame = Frame(parent,)
        frame.place(x=43, y=60, width=213, height=181)
        return frame
    def __tk_label_m0t2kqaf(self,parent):
        label = Label(parent,text="标签",anchor="center", )
        label.place(x=0, y=10, width=50, height=30)
        return label
    def __tk_input_m0t2kvni(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=0, y=60, width=150, height=30)
        return ipt
    def __tk_button_m0t2kyjw(self,parent):
        btn = Button(parent, text="按钮", takefocus=False,)
        btn.place(x=0, y=130, width=50, height=30)
        return btn
    def __tk_button_m0t2l0z9(self,parent):
        btn = Button(parent, text="按钮", takefocus=False,)
        btn.place(x=60, y=130, width=50, height=30)
        return btn
    def __tk_frame_m0t2le6k(self,parent):
        frame = Frame(parent,)
        frame.place(x=299, y=57, width=259, height=187)
        return frame
    def __tk_text_m0t2lo9i(self,parent):
        text = Text(parent)
        text.place(x=0, y=10, width=150, height=100)
        return text
    def __tk_progressbar_m0t2lrxa(self,parent):
        progressbar = Progressbar(parent, orient=HORIZONTAL,)
        progressbar.place(x=0, y=120, width=150, height=30)
        return progressbar
    def __tk_check_button_m0t2lvon(self,parent):
        cb = Checkbutton(parent,text="多选框",)
        cb.place(x=160, y=10, width=80, height=33)
        return cb
    def __tk_radio_button_m0t2m2qb(self,parent):
        rb = Radiobutton(parent,text="单选框",)
        rb.place(x=158, y=88, width=80, height=30)
        return rb
    def __tk_radio_button_m0t2m5u0(self,parent):
        rb = Radiobutton(parent,text="单选框",)
        rb.place(x=159, y=121, width=80, height=30)
        return rb
    def __tk_check_button_m0t2matm(self,parent):
        cb = Checkbutton(parent,text="多选框",)
        cb.place(x=160, y=40, width=80, height=30)
        return cb
    def __tk_label_frame_m0t2mle2(self,parent):
        frame = LabelFrame(parent,text="标签容器",)
        frame.place(x=39, y=262, width=251, height=150)
        return frame
    def __tk_check_button_m0t2mzao(self,parent):
        cb = Checkbutton(parent,text="多选框",)
        cb.place(x=0, y=0, width=80, height=30)
        return cb
    def __tk_check_button_m0t2n1gt(self,parent):
        cb = Checkbutton(parent,text="多选框",)
        cb.place(x=0, y=30, width=80, height=30)
        return cb
    def __tk_check_button_m0t2n3mm(self,parent):
        cb = Checkbutton(parent,text="多选框",)
        cb.place(x=0, y=60, width=80, height=30)
        return cb
    def __tk_select_box_m0t2n6rv(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("列表框","Python","Tkinter Helper")
        cb.place(x=89, y=0, width=116, height=30)
        return cb
    def __tk_scale_m0t2ng1s(self,parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(x=90, y=60, width=150, height=30)
        return scale
    def __tk_button_m0t2nl04(self,parent):
        btn = Button(parent, text="按钮", takefocus=False,)
        btn.place(x=0, y=90, width=50, height=30)
        return btn
# class Win(WinGUI):
#     def __init__(self, controller):
#         self.ctl = controller
#         super().__init__()
#         self.__event_bind()
#         self.__style_config()
#         self.ctl.init(self)
#     def __event_bind(self):
#         pass
#     def __style_config(self):
#         pass
if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()