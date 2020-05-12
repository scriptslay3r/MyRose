    # Imports #
import tkinter as tk

    # Main #
def main():
    tk_Root = tk.Tk()
    tk_Root.title("Named Color Chart")
    tk_Chart = c_ColorChart(tk_Root, l_Colors)
    tk_Root.mainloop()

#-----------Basement------------
    # Classes #
class c_ColorChart(tk.Frame):
    v_Rows = 36
    v_FontSize = 6

    def __init__(self, tk_Root, l_Colors):
        tk.Frame.__init__(self, tk_Root)
        v_Row = 0
        v_Column = 0

        for _Color in l_Colors:
            tk_Label = tk.Label(self, text=_Color, bg=_Color,\
            font=("Times", self.v_FontSize, "bold"))
            tk_Label.grid(row=v_Row, column=v_Column, sticky="ew")
            v_Row += 1

            if v_Row > self.v_Rows:
                v_Row = 0
                v_Column += 1

        self.pack(expand=1, fill="both")

l_Colors = ["MAROON","DARKRED","BROWN","FIREBRICK","CRIMSON","RED","TOMATO",
"CORAL","INDIANRED","LIGHTCORAL","DARKSALMON","SALMON","LIGHTSALMON","ORANGERED",
"DARKORANGE","ORANGE","GOLD","DARKGOLDENROD","GOLDENROD","PALEGOLDENROD",
"DARKKHAKI","KHAKI","OLIVE","YELLOW","YELLOWGREEN","DARKOLIVEGREEN","OLIVEDRAB",
"LAWNGREEN","CHARTREUSE","GREENYELLOW","DARKGREEN","GREEN","FORESTGREEN","LIME",
"LIMEGREEN","LIGHTGREEN","PALEGREEN","DARKSEAGREEN","MEDIUMSPRINGGREEN",
"SPRINGGREEN","SEAGREEN","MEDIUMAQUAMARINE","MEDIUMSEAGREEN","LIGHTSEAGREEN",
"DARKSLATEGRAY","TEAL","DARKCYAN","AQUA","CYAN","LIGHTCYAN","DARKTURQUOISE",
"TURQUOISE","MEDIUMTURQUOISE","PALETURQUOISE","AQUAMARINE","POWDERBLUE","CADETBLUE",
"STEELBLUE","CORNFLOWERBLUE","DEEPSKYBLUE","DODGERBLUE","LIGHTBLUE","SKYBLUE",
"LIGHTSKYBLUE","MIDNIGHTBLUE","NAVY","DARKBLUE","MEDIUMBLUE","BLUE","ROYALBLUE",
"BLUEVIOLET","INDIGO","DARKSLATEBLUE","SLATEBLUE","MEDIUMSLATEBLUE","MEDIUMPURPLE",
"DARKMAGENTA","DARKVIOLET","DARKORCHID","MEDIUMORCHID","PURPLE","THISTLE","PLUM",
"VIOLET","MAGENTA","ORCHID","MEDIUMVIOLETRED","PALEVIOLETRED","DEEPPINK","HOTPINK",
"LIGHTPINK","PINK","ANTIQUEWHITE","BEIGE","BISQUE","BLANCHEDALMOND","WHEAT","CORNSILK",
"LEMONCHIFFON","LIGHTGOLDENRODYELLOW","LIGHTYELLOW","SADDLEBROWN","SIENNA","CHOCOLATE",
"PERU","SANDYBROWN","BURLYWOOD","TAN","ROSYBROWN","MOCCASIN","NAVAJOWHITE","PEACHPUFF",
"MISTYROSE","LAVENDERBLUSH","LINEN","OLDLACE","PAPAYAWHIP","SEASHELL","MINTCREAM",
"SLATEGRAY","LIGHTSLATEGRAY","LIGHTSTEELBLUE","LAVENDER","FLORALWHITE","ALICEBLUE",
"GHOSTWHITE","HONEYDEW","IVORY","AZURE","SNOW","BLACK","DIMGRAY","GRAY","DARKGRAY",
"SILVER","LIGHTGRAY","GAINSBORO","WHITESMOKE","WHITE"]

    # Main Loop #
if __name__ == '__main__':
    main()