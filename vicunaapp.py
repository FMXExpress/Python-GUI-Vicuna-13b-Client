from delphifmx import *
import replicate
import urllib.request
import hashlib
import os
os.environ["REPLICATE_API_TOKEN"] = ""

class Vicuna13bForm(Form):

    def __init__(self, owner):
        self.stylemanager = StyleManager(self)
        self.stylemanager.SetStyleFromFile("Air.style")

        self.SetProps(Caption="Vicuna 13b + Replicate API", OnShow=self.__form_show, OnClose=self.__form_close)

        self.layout_top = Layout(self)
        self.layout_top.SetProps(Parent=self, Align="Top", Height="50", Margins = Bounds(RectF(3, 3, 3, 3)))

        self.prompt_label = Label(self)
        self.prompt_label.SetProps(Parent=self.layout_top, Align="Left", Text="Prompt:", Position=Position(PointF(20, 20)), Margins = Bounds(RectF(3, 3, 3, 3)))

        self.prompt_edit = Edit(self)
        self.prompt_edit.SetProps(Parent=self.layout_top, Align="Client", Text="What is Embarcadero Delphi?", Position=Position(PointF(80, 18)), Width=200, Margins = Bounds(RectF(3, 3, 3, 3)))

        self.generate_button = Button(self)
        self.generate_button.SetProps(Parent=self.layout_top, Align = "Right", Text="Generate", Position=Position(PointF(290, 18)), Width=80, OnClick=self.__button_click, Margins = Bounds(RectF(3, 3, 3, 3)))

        self.memo_control = Memo(self)
        self.memo_control.SetProps(Parent=self, Align="Client", WordWrap="True", Position=Position(PointF(20, 60)), Width=350, Height=350, Margins = Bounds(RectF(3, 3, 3, 3)))

    def __form_show(self, sender):
        self.SetProps(Width=640, Height=480)

    def __form_close(self, sender, action):
        action = "caFree"

    def __button_click(self, sender):
        prompt = self.prompt_edit.text
        self.memo_control.Lines.Text = ""
        output = replicate.run(
            "replicate/vicuna-13b:a68b84083b703ab3d5fbf31b6e25f16be2988e4c3e21fe79c2ff1c18b99e61c1",
            input={"prompt": prompt, "max_length":50, "repetition_penalty":1, "temperature":0.75, "top_p":1}
        )
        for item in output:
                self.memo_control.Lines.Text = self.memo_control.Lines.Text + item

def main():
    Application.Initialize()
    Application.Title = "Vicuna 13b + Replicate API"
    Application.MainForm = Vicuna13bForm(Application)
    Application.MainForm.Show()
    Application.Run()
    Application.MainForm.Destroy()

if __name__ == '__main__':
    main()